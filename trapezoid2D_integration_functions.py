# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:40:54 2020

@author: Fer Caprile

Functions for simulation of the diffraction obtained by an arbitrary phase mask
"""

import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
from scipy.optimize import minimize_scalar as minim

def generate_incident_field(maskfunction,alpha,focus,resolution_phi,resolution_theta,h,psi,delta,radius,I0,wavelength):
    '''
    Generate a matrix for the field X and Y direction of the incident field on the lens, given the respective maskfunction
    
    This matrix has the value of the amplitude of the incident field for each value of theta and phi
    '''

    k=2*np.pi/wavelength
    gaussian= lambda rho: np.exp(-(rho/radius)**2)
    ex_lens=np.zeros((resolution_phi,resolution_theta),dtype=complex)
    ey_lens=np.zeros((resolution_phi,resolution_theta),dtype=complex)

    theta_values=np.linspace(0,alpha,resolution_theta)  #divisions of theta in which the trapezoidal 2D integration is done
    rhop_values=np.sin(theta_values)*focus              #given by the sine's law
    phip_values=np.linspace(0,2*np.pi,resolution_phi)   #divisions of phi in which the trapezoidal 2D integration is done
    for i,phip in enumerate(phip_values):
        for j,rhop in enumerate(rhop_values):
            phase=maskfunction(rhop,phip,radius,focus,k)
            ex_lens[i,j]=gaussian(rhop)*phase
            ey_lens[i,j]=gaussian(rhop)*phase
    ex_lens*=np.cos(psi*np.pi/180)*I0**0.5
    ey_lens*=np.sin(psi*np.pi/180)*np.exp(1j*delta*np.pi/180)*I0**0.5
    return ex_lens,ey_lens

def plot_in_cartesian(Ex,Ey,xmax,alpha,focus,figure_name):
    '''
    Plot the fields Ex and Ey, who are described in polar coordinates 
    '''
    resolution_phi,resolution_theta=np.shape(Ex)
    x_values=np.linspace(-xmax,xmax,2*resolution_theta) #positions along X in which to plot
    y_values=np.linspace(xmax,-xmax,2*resolution_theta)
    I_cartesian=np.zeros((2*resolution_theta,2*resolution_theta))
    Ex_cartesian=np.zeros((2*resolution_theta,2*resolution_theta),dtype=complex)
    Ey_cartesian=np.zeros((2*resolution_theta,2*resolution_theta),dtype=complex)
    
    #original polar coordinates in which the Ex and Ey where calculated:  
    theta_values=np.linspace(0,alpha,resolution_theta)  #divisions of theta in which the trapezoidal 2D integration is done
    rhop_values=np.sin(theta_values)*focus              #given by the sine's law
    phip_values=np.linspace(0,2*np.pi,resolution_phi)   #divisions of phi in which the trapezoidal 2D integration is done
    
    #passage from polar to cartesian coordinates, keep in mind the positions are not to be exact since the plot is on a grid
    for i,x in enumerate(x_values):
        for j,y in enumerate(y_values):
            rhop=(x**2+y**2)**0.5
            phip=np.arctan2(y,x)
            if phip<0:
                phip+=2*np.pi
            if rhop<xmax:
                id_rho = (np.abs(rhop_values - rhop)).argmin() #get the closest indent for the coordinate in which the field was calculated
                id_phi = (np.abs(phip_values - phip)).argmin()
                Ex_cartesian[j,i]=Ex[id_phi,id_rho]
                Ey_cartesian[j,i]=Ey[id_phi,id_rho]

    I_cartesian=np.abs(Ex_cartesian)**2+np.abs(Ey_cartesian)**2
    
    #colorbar plot for the field:
    plt.rcParams['font.size']=20#tamaño de fuente
    fig1, (ax1, ax2) = plt.subplots(num=str(figure_name)+': Incident intensity',figsize=(12, 5), ncols=2)
    fig1.suptitle('Field at the objective using 2D integration')
    
    ax1.set_title('Intensity')
    pos=ax1.imshow(I_cartesian,extent=[-xmax,xmax,-xmax,xmax], interpolation='none', aspect='auto')
    ax1.set_xlabel('x (mm)')
    ax1.set_ylabel('y (mm)')
    ax1.axis('square')
    cbar1= fig1.colorbar(pos, ax=ax1)
    cbar1.ax.set_ylabel('Intensity (kW/cm\u00b2)')            
    #plot along the Y=0 axis:
    ax2.set_title(' Intensity along x')
    ax2.plot(np.linspace(-xmax,xmax,2*resolution_theta),I_cartesian[resolution_theta,:])
    ax2.set_xlabel('x (mm)')
    ax2.set_ylabel('Intensity  (kW/cm\u00b2)')  
    fig1.tight_layout()
    fig1.subplots_adjust(top=0.80)                
    
    #Amplitude and phase plot 
    #Ex
    fig2, ((ax_x1,ax_y1),(ax_x2,ax_y2)) = plt.subplots(num=str(figure_name)+': Incident amplitude',figsize=(12, 8),nrows=2, ncols=2)
    ax_x1.set_title('ex amplitude')
    pos_x1=ax_x1.imshow(np.abs(Ex_cartesian),extent=[-xmax,xmax,-xmax,xmax], interpolation='none', aspect='equal')
    ax_x1.set_xlabel('x (mm)')
    ax_x1.set_ylabel('y (mm)')
    ax_x1.axis('square')
    cbar_1_1=fig2.colorbar(pos_x1, ax=ax_x1)
    cbar_1_1.ax.set_ylabel('Amplitude')
    
    ax_x2.set_title('ex phase')
    pos_x2=ax_x2.imshow(np.angle(Ex_cartesian),extent=[-xmax,xmax,-xmax,xmax], interpolation='none', aspect='equal')
    ax_x2.set_xlabel('x (mm)')
    ax_x2.set_ylabel('y (mm)')
    ax_x2.axis('square')
    cbar_1_1=fig2.colorbar(pos_x2, ax=ax_x2)
    cbar_1_1.ax.set_ylabel('Angle (Radians)')
    
    #Ey
    ax_y1.set_title('ey amplitude')
    pos_y1=ax_y1.imshow(np.abs(Ey_cartesian),extent=[-xmax,xmax,-xmax,xmax], interpolation='none', aspect='equal')
    ax_y1.set_xlabel('x (mm)')
    ax_y1.set_ylabel('y (mm)')
    ax_y1.axis('square')
    cbar_1_1=fig2.colorbar(pos_y1, ax=ax_y1)
    cbar_1_1.ax.set_ylabel('Amplitude')
    
    ax_y2.set_title('ey phase')
    pos_y2=ax_y2.imshow(np.angle(Ey_cartesian),extent=[-xmax,xmax,-xmax,xmax], interpolation='none', aspect='equal')
    ax_y2.set_xlabel('x (mm)')
    ax_y2.set_ylabel('y (mm)')
    ax_y2.axis('square')
    cbar_1_1=fig2.colorbar(pos_y2, ax=ax_y2)
    cbar_1_1.ax.set_ylabel('Angle (Radians)')
    
    fig2.tight_layout()
    
    return I_cartesian,Ex_cartesian,Ey_cartesian

def custom_mask_objective_field(psi,delta,resolution_theta,resolution_phi,N_rho,N_phi,alpha,mask_function,h,L,I0,Lambda,radius,fig_name,plot=True):
    '''
    Difraction for an arbitrary phase mask under the paraxial approximation, using the GPU
    
    The resultant matrix Ex and Ey are outputed in polar coordinates (each row is a different value of phi and each column a different rho)  
    '''
    
    print('Calculating field at the objective:')
    time.sleep(0.2)
    focus=h/np.sin(alpha)
    
    #define divisions for the integration:
    rho_values=np.linspace(0,h,N_rho)
    phi_values=np.linspace(0,2*np.pi,N_phi)
    rho,phi=np.meshgrid(rho_values,phi_values)
    
    #2D trapezoidal method weight:
    h_rho=h/N_rho
    h_phi=2*np.pi/N_phi
    weight_rho=np.zeros(N_rho)+h_rho
    weight_rho[0]=h_rho/2
    weight_rho[-1]=h_rho/2
    weight_phi=np.zeros(N_phi)+h_phi
    weight_phi[0]=h_phi/2
    weight_phi[-1]=h_phi/2
    weight=weight_rho*np.vstack(weight_phi)

    #define coordinates in which to calculate the field:    
    theta_values=np.linspace(0,alpha,resolution_theta)  #divisions of theta in which the trapezoidal 2D integration is done
    rhop_values=np.sin(theta_values)*focus              #given by the sine's law
    phip_values=np.linspace(0,2*np.pi,resolution_phi)   #divisions of phi in which the trapezoidal 2D integration is done

    #Define function to integrate and field matrix:    
    Ex=np.zeros((resolution_phi,resolution_theta),dtype=complex)
    kl=np.pi/Lambda/L
    '''
    #the function to integrate is:
    f=lambda rho,phi: rho*np.exp(-(rho/radius)**2)*mask_function(rho,phi)*np.exp(1j*(kl*(rho**2-2*rho*rhop*np.cos(phi-phip))))
    '''
    
    k=2*np.pi/Lambda
    #in order to save computing time, i do separatedly the calculation of terms that would otherwise e claculated multiple times, since they do not depend on rhop,phip (the coordinates at which the field is calculated)
    prefactor=rho*np.exp(-(rho/radius)**2+1j*(k*L+kl*rho**2))*mask_function(rho,phi,radius,focus,k)*weight
    #numerical 2D integration: 
    for j in tqdm(range(resolution_phi)):
        phip=phip_values[j]
        for i,rhop in enumerate(rhop_values):
            phase=np.exp(1j*k*rhop**2/2/L)*np.exp(-1j*kl*(2*rho*rhop*np.cos(phi-phip)))         
            Ex[j,i]=np.sum(prefactor*phase)
    
    Ex*=-1j/Lambda/L
    
    #on this approximation, the field in the Y direction is the same as the field on the X direction with a different global phase and amplitude        
    Ey=Ex*np.exp(1j*np.pi/180*delta)
    Ex*=np.cos(np.pi/180*psi)*I0**0.5
    Ey*=np.sin(np.pi/180*psi)*I0**0.5
    
    I_cartesian,Ex_cartesian,Ey_cartesian=plot_in_cartesian(Ex,Ey,h,alpha,focus,fig_name)
        
    return Ex,Ey,I_cartesian,Ex_cartesian,Ey_cartesian

def test_custom_mask_objective_field(psi,delta,resolution_theta,resolution_phi,N_rho,N_phi,alpha,mask_function,h,L,I0,Lambda,radius,plot=True):
    '''
    Quick run for testing if the resolution used to do the 2D integration is high enought.
    Meant for difraction for an arbitrary phase mask under the paraxial approximation, using the GPU
    '''
    print('Calculating field at the objective:')
    time.sleep(0.2)
    focus=h/np.sin(alpha)
    
    #define divisions for the integration:
    rho_values=np.linspace(0,h,N_rho)
    phi_values=np.linspace(0,2*np.pi,N_phi)
    rho,phi=np.meshgrid(rho_values,phi_values)
    
    #2D trapezoidal method weight:
    h_rho=h/N_rho
    h_phi=2*np.pi/N_phi
    weight_rho=np.zeros(N_rho)+h_rho
    weight_rho[0]=h_rho/2
    weight_rho[-1]=h_rho/2
    weight_phi=np.zeros(N_phi)+h_phi
    weight_phi[0]=h_phi/2
    weight_phi[-1]=h_phi/2
    weight=weight_rho*np.vstack(weight_phi)
    
    resolution_phi=int(resolution_phi/20) #only make 1/20 of the total calculation
    #define coordinates in which to calculate the field:    
    theta_values=np.linspace(0,alpha,resolution_theta)    
    rhop_values=np.sin(theta_values)*focus
    phip_values=np.linspace(0,np.pi/20,resolution_phi)

    #Define function to integrate and field matrix:    
    Ex=np.zeros((resolution_phi,resolution_theta),dtype=complex)
    kl=np.pi/Lambda/L
    '''
    #the function to integrate is:
    f=lambda rho,phi: rho*np.exp(-(rho/radius)**2)*mask_function(rho,phi)*np.exp(1j*(kl*(rho**2-2*rho*rhop*np.cos(phi-phip))))
    '''
    k=2*np.pi/Lambda
    #in order to save computing time, i do separatedly the calculation of terms that would otherwise e claculated multiple times, since they do not depend on rhop,phip (the coordinates at which the field is calculated)
    prefactor=rho*np.exp(-(rho/radius)**2)*mask_function(rho,phi)*weight

    #numerical 2D integration: 
    for j in tqdm(range(resolution_phi)):
        phip=phip_values[j]
        for i,rhop in enumerate(rhop_values):
            phase=np.exp(1j*k*(L+rhop**2/2/L))*np.exp(1j*(kl*(rho**2-2*rho*rhop*np.cos(phi-phip))))         
            Ex[j,i]=np.sum(prefactor*phase)
    
    Ex*=-1j/Lambda/L

    #on this approximation, the field in the Y direction is the same as the field on the X direction with a different global phase and amplitude        
    Ey=Ex*np.exp(1j*np.pi/180*delta)
    Ex*=np.cos(np.pi/180*psi)*I0**0.5
    Ey*=np.sin(np.pi/180*psi)*I0**0.5

    I_cartesian,Ex_cartesian,Ey_cartesian=plot_in_cartesian(Ex,Ey,h,alpha,focus)

    return Ex,Ey,I_cartesian,Ex_cartesian,Ey_cartesian

def custom_mask_focus_field(ex_lens,ey_lens,alpha,h,Lambda,zp0,resolution_focus,resolution_theta,resolution_phi,FOV_focus,countdown=True,x0=0,y0=0):
    '''
    High apperture difraction for an arbitrary incident field. Only calculates the field on the XY focal plane.
    
    countdown=True means you are only running this fuction once and you want to see te time elapsed and expected to finish the calculation
    
    x0 and y0 are used for calculating the field centered at an x0, y0 position
    '''
    
    if countdown==True:
        print('Calculating field at the focal plane:')
        time.sleep(0.5)
    Lambda*=10**6
    focus=h/np.sin(alpha)*10**6
        
    #The X component of incident field must be evaluated at phi-pi, which is equivalent to moving the rows of the matrix    
    def rotate_180º(matrix):
        a,b=np.shape(matrix)       
        aux=np.zeros((a,b),dtype=complex)        
        for i in range(a):
            aux[i-int(a/2),:]=matrix[i,:]
        return aux
    #The Y component of incident field must be evaluated at phi-pi-pi/2, which is equivalent to moving the rows of the matrix    
    def rotate_270º(matrix):
        a,b=np.shape(matrix)       
        aux=np.zeros((a,b),dtype=complex)        
        for i in range(a):
            aux[i-int(3*a/4),:]=matrix[i,:]
        return aux

    ex_lens=rotate_180º(ex_lens)        
    ey_lens=rotate_270º(ey_lens)
    
    '''
    # the functions i am going to integrate are:
    fun1=lambda phi,theta: np.cos(theta)**0.5*np.sin(theta)*(np.cos(theta) + (1 - np.cos(theta))*np.sin(phi)**2)*np.exp(1j*(np.sin(theta)*kr*np.cos(phi - phip) + np.cos(theta)*kz))
    fun2=lambda phi,theta: np.cos(theta)**0.5*np.sin(theta)*(1 - np.cos(theta))*np.cos(phi)*np.sin(phi)*np.exp(1j*(np.sin(theta)*kr*np.cos(phi - phip) + np.cos(theta)*kz))
    fun3=lambda phi,theta: np.cos(theta)**0.5*np.sin(theta)**2*np.cos(phi)*np.exp(1j*(np.sin(theta)*kr*np.cos(phi - phip) + np.cos(theta)*kz))
    fun4=lambda phi,theta: np.cos(theta)**0.5*np.sin(theta)*(1 - np.cos(theta))*np.cos(phi)*np.sin(phi)*np.exp(1j*(-np.sin(theta)*kr*np.sin(phi - phip) + np.cos(theta)*kz))
    fun5=lambda phi,theta: np.cos(theta)**0.5*np.sin(theta)*(np.cos(theta) + (1 - np.cos(theta))*np.sin(phi)**2)*np.exp(1j*(-np.sin(theta)*kr*np.sin(phi - phip) + np.cos(theta)*kz))
    fun6=lambda phi,theta: np.cos(theta)**0.5*np.sin(theta)**2*np.cos(phi)*np.exp(1j*(-np.sin(theta)*kr*np.sin(phi - phip) + np.cos(theta)*kz))
    '''  
    #2D trapezoidal method weight:
    h_theta=alpha/resolution_theta
    h_phi=2*np.pi/resolution_phi
    weight_trapezoid_rho=np.zeros(resolution_theta)+h_theta
    weight_trapezoid_rho[0]=h_theta/2
    weight_trapezoid_rho[-1]=h_theta/2
    weight_trapezoid_phi=np.zeros(resolution_phi)+h_phi
    weight_trapezoid_phi[0]=h_phi/2
    weight_trapezoid_phi[-1]=h_phi/2
    weight_trapezoid=weight_trapezoid_rho*np.vstack(weight_trapezoid_phi)#represents the area of each trapezoid for each position in phi,theta
    
    #define coordinates in which to calculate the field:    
    xmax=FOV_focus/2
    x_values=np.linspace(-xmax+x0,xmax+x0,resolution_focus)
    y_values=np.linspace(xmax+y0,-xmax+y0,resolution_focus)
    ex=np.zeros((resolution_focus,resolution_focus),dtype=complex)
    ey=np.copy(ex)
    ez=np.copy(ex)
    
    #define divisions for the integration:
    theta_values=np.linspace(0,alpha,resolution_theta)    #divisions of theta in which the trapezoidal 2D integration is done
    phi_values=np.linspace(0,2*np.pi,resolution_phi)      #divisions of phi in which the trapezoidal 2D integration is done
    theta,phi=np.meshgrid(theta_values,phi_values)        #turn the divisions into a matrix in order to apply the function more easily

    kz=zp0*2*np.pi/Lambda

    #now begins the integration, in order to save computing time i do the trigonometric functions separatedly and save the value into another variable
    cos_theta=np.cos(theta)
    cos_theta_sqrt=cos_theta**0.5
    sin_theta=np.sin(theta)
    cos_phi=np.cos(phi)
    sin_phi=np.sin(phi)
    sin_phi_square=sin_phi**2
    
    prefactor_general=cos_theta_sqrt*sin_theta
    prefactor_x=prefactor_general*(cos_theta+(1-cos_theta)*sin_phi_square)
    prefactor_y=prefactor_general*(1-cos_theta)*cos_phi*sin_phi
    prefactor_z=prefactor_general*sin_theta*cos_phi
    
    Axx=prefactor_x*ex_lens*weight_trapezoid
    Axy=prefactor_y*ex_lens*weight_trapezoid
    Axz=prefactor_z*ex_lens*weight_trapezoid

    Ayx=prefactor_y*ey_lens*weight_trapezoid
    Ayy=-prefactor_x*ey_lens*weight_trapezoid
    Ayz=prefactor_z*ey_lens*weight_trapezoid

    cos_theta_kz=cos_theta*kz
    #now for each position in which i calculate the field i do the integration
    if countdown==True:
        for i in tqdm(range(resolution_focus),desc='XY plane'):
            x=x_values[i]
            for j,y in enumerate(y_values):#idea, rotar en phi es correr las columnas de la matriz ex, ey
                rhop=(x**2+y**2)**0.5
                phip=np.arctan2(y,x)
                kr=rhop*2*np.pi/Lambda
                sin_theta_kr=sin_theta*kr
                phase_inc_x=np.exp(1j*(sin_theta_kr*np.cos(phi - phip) + cos_theta_kz))#phase for the X incident component
                phase_inc_y=np.exp(1j*(-sin_theta_kr*np.sin(phi - phip) + cos_theta_kz))#phase for the Y incident component
                #now, the integration is made as the sum of the value of the integrand in each position of phi,theta:
                ex[j,i]=np.sum(Axx*phase_inc_x)+np.sum(Ayx*phase_inc_y) 
                ey[j,i]=np.sum(Axy*phase_inc_x)+np.sum(Ayy*phase_inc_y)
                ez[j,i]=np.sum(Axz*phase_inc_x)+np.sum(Ayz*phase_inc_y)
    else:
        for i,x in enumerate(x_values):
            for j,y in enumerate(y_values):
                rhop=(x**2+y**2)**0.5
                phip=np.arctan2(y,x)
                kr=rhop*2*np.pi/Lambda
                sin_theta_kr=sin_theta*kr
                phase_inc_x=np.exp(1j*(sin_theta_kr*np.cos(phi - phip) + cos_theta_kz))#phase for the X incident component
                phase_inc_y=np.exp(1j*(-sin_theta_kr*np.sin(phi - phip) + cos_theta_kz))#phase for the Y incident component
                #now, the integration is made as the sum of the value of the integrand in each position of phi,theta:
                ex[j,i]=np.sum(Axx*phase_inc_x)+np.sum(Ayx*phase_inc_y)
                ey[j,i]=np.sum(Axy*phase_inc_x)+np.sum(Ayy*phase_inc_y)
                ez[j,i]=np.sum(Axz*phase_inc_x)+np.sum(Ayz*phase_inc_y)
        
    ex*=-1j*focus/Lambda
    ey*=1j*focus/Lambda
    ez*=1j*focus/Lambda
    
    return ex,ey,ez

def custom_mask_focus_field_XZ_XY(ex_lens,ey_lens,alpha,h,Lambda,z_FOV,resolution_z,zp0,resolution_focus,resolution_theta,resolution_phi,FOV_focus,x0=0,y0=0,plot_plane='X'):
    '''
    High apperture difraction for an arbitrary incident field. Calculates the field on the XY and XZ focal planes.
        
    x0 and y0 are used for calculating the field centered at an x0, y0 position
    
    plot_plane='X' is used for calculating the XZ plane, otherwise plot_plane='Y' calculates the YZ plane
    '''
    #XY plane: 
    Ex_XY,Ey_XY,Ez_XY=custom_mask_focus_field(ex_lens,ey_lens,alpha,h,Lambda,zp0,resolution_focus,resolution_theta,resolution_phi,FOV_focus,countdown=True,x0=x0,y0=y0)
    
    #XZ plane:
    if int(resolution_z%2)==0:
        resolution_z+=1    #make the middle coordinate on Z be Z=0
        
    Lambda*=10**6               #passage from mm to nm
    focus=h/np.sin(alpha)*10**6 #passage from mm to nm
        
    #The X component of incident field must be evaluated at phi-pi, which is equivalent to moving the rows of the matrix    
    def rotate_180º(matrix):
        a,b=np.shape(matrix)       
        aux=np.zeros((a,b),dtype=complex)        
        for i in range(a):
            aux[i-int(a/2),:]=matrix[i,:]
        return aux
    #The Y component of incident field must be evaluated at phi-pi-pi/2, which is equivalent to moving the rows of the matrix    
    def rotate_270º(matrix):
        a,b=np.shape(matrix)       
        aux=np.zeros((a,b),dtype=complex)        
        for i in range(a):
            aux[i-int(3*a/4),:]=matrix[i,:]
        return aux

    ex_lens=rotate_180º(ex_lens)        
    ey_lens=rotate_270º(ey_lens)

    '''
    # the functions i am going to integrate are:
    fun1=lambda theta, phi: np.cos(theta)**0.5*np.sin(theta)*(np.cos(theta) + (1 - np.cos(theta))*np.sin(phi)**2)*np.exp(1j*(np.sin(theta)*kr*np.cos(phi - phip) + np.cos(theta)*kz))
    fun2=lambda theta, phi: np.cos(theta)**0.5*np.sin(theta)*(1 - np.cos(theta))*np.cos(phi)*np.sin(phi)*np.exp(1j*(np.sin(theta)*kr*np.cos(phi - phip) + np.cos(theta)*kz))
    fun3=lambda theta, phi: np.cos(theta)**0.5*np.sin(theta)**2*np.cos(phi)*np.exp(1j*(np.sin(theta)*kr*np.cos(phi - phip) + np.cos(theta)*kz))
    fun4=lambda theta, phi: np.cos(theta)**0.5*np.sin(theta)*(1 - np.cos(theta))*np.cos(phi)*np.sin(phi)*np.exp(1j*(-np.sin(theta)*kr*np.sin(phi - phip) + np.cos(theta)*kz))
    fun5=lambda theta, phi: np.cos(theta)**0.5*np.sin(theta)*(np.cos(theta) + (1 - np.cos(theta))*np.sin(phi)**2)*np.exp(1j*(-np.sin(theta)*kr*np.sin(phi - phip) + np.cos(theta)*kz))
    fun6=lambda theta, phi: np.cos(theta)**0.5*np.sin(theta)**2*np.cos(phi)*np.exp(1j*(-np.sin(theta)*kr*np.sin(phi - phip) + np.cos(theta)*kz))
    '''  
        
    #2D trapezoidal method weight:
    h_theta=alpha/resolution_theta
    h_phi=2*np.pi/resolution_phi
    weight_trapezoid_rho=np.zeros(resolution_theta)+h_theta
    weight_trapezoid_rho[0]=h_theta/2
    weight_trapezoid_rho[-1]=h_theta/2
    weight_trapezoid_phi=np.zeros(resolution_phi)+h_phi
    weight_trapezoid_phi[0]=h_phi/2
    weight_trapezoid_phi[-1]=h_phi/2
    weight_trapezoid=weight_trapezoid_rho*np.vstack(weight_trapezoid_phi) #represents the area of each trapezoid for each position in phi,theta

    #define coordinates in which to calculate the field:                
    xmax=FOV_focus*2**0.5/2  #I want to plot up to FOV*2**0.5
    x_values=np.linspace(-xmax+x0,xmax+x0,resolution_focus)
    z_values=np.linspace(z_FOV/2,-z_FOV/2,resolution_z)
    
    Ex_XZ=np.zeros((resolution_z,resolution_focus),dtype=complex)
    Ey_XZ=np.copy(Ex_XZ)
    Ez_XZ=np.copy(Ex_XZ)
        
    #define divisions for the integration:
    theta_values=np.linspace(0,alpha,resolution_theta)    #divisions of theta in which the trapezoidal 2D integration is done
    phi_values=np.linspace(0,2*np.pi,resolution_phi)      #divisions of phi in which the trapezoidal 2D integration is done
    theta,phi=np.meshgrid(theta_values,phi_values)        #turn the divisions into a matrix in order to apply the function more easily
    
    #now begins the integration, in order to save computing time i do the trigonometric functions separatedly and save the value into another variable
    cos_theta=np.cos(theta)
    cos_theta_sqrt=cos_theta**0.5
    sin_theta=np.sin(theta)
    cos_phi=np.cos(phi)
    sin_phi=np.sin(phi)
    sin_phi_square=sin_phi**2
    
    prefactor_general=cos_theta_sqrt*sin_theta
    prefactor_x=prefactor_general*(cos_theta+(1-cos_theta)*sin_phi_square)
    prefactor_y=prefactor_general*(1-cos_theta)*cos_phi*sin_phi
    prefactor_z=prefactor_general*sin_theta*cos_phi

    Axx=prefactor_x*ex_lens*weight_trapezoid
    Axy=prefactor_y*ex_lens*weight_trapezoid
    Axz=prefactor_z*ex_lens*weight_trapezoid

    Ayx=prefactor_y*ey_lens*weight_trapezoid
    Ayy=-prefactor_x*ey_lens*weight_trapezoid
    Ayz=prefactor_z*ey_lens*weight_trapezoid

    if plot_plane=='X':
        for j in tqdm(range(resolution_z),desc='XZ plane'):
            zp0=z_values[j]
            for i,x in enumerate(x_values):#idea, rotar en phi es correr las columnas de la matriz ex, ey
                rhop=np.abs(x)
                phip=np.arctan2(0,x)
                kr=rhop*2*np.pi/Lambda
                kz=zp0*2*np.pi/Lambda
                sin_theta_kr=sin_theta*kr
                cos_theta_kz=cos_theta*kz
                phase_inc_x=np.exp(1j*(sin_theta_kr*np.cos(phi - phip) + cos_theta_kz))#phase for the X incident component
                phase_inc_y=np.exp(1j*(-sin_theta_kr*np.sin(phi - phip) + cos_theta_kz))#phase for the Y incident component
                #now, the integration is made as the sum of the value of the integrand in each position of phi,theta:
                Ex_XZ[j,i]=np.sum(Axx*phase_inc_x)+np.sum(Ayx*phase_inc_y)
                Ey_XZ[j,i]=np.sum(Axy*phase_inc_x)+np.sum(Ayy*phase_inc_y)
                Ez_XZ[j,i]=np.sum(Axz*phase_inc_x)+np.sum(Ayz*phase_inc_y)
    else:
        if plot_plane=='Y':           
            for j in tqdm(range(resolution_z),desc='YZ plane'):
                zp0=z_values[j]
                for i,y in enumerate(x_values):#idea, rotar en phi es correr las columnas de la matriz ex, ey
                    rhop=np.abs(y)
                    phip=np.arctan2(y,0)
                    kr=rhop*2*np.pi/Lambda
                    kz=zp0*2*np.pi/Lambda
                    sin_theta_kr=sin_theta*kr
                    cos_theta_kz=cos_theta*kz
                    phase_inc_x=np.exp(1j*(sin_theta_kr*np.cos(phi - phip) + cos_theta_kz))#phase for the X incident component
                    phase_inc_y=np.exp(1j*(-sin_theta_kr*np.sin(phi - phip) + cos_theta_kz))#phase for the Y incident component
                    #now, the integration is made as the sum of the value of the integrand in each position of phi,theta:
                    Ex_XZ[j,i]=np.sum(Axx*phase_inc_x)+np.sum(Ayx*phase_inc_y)
                    Ey_XZ[j,i]=np.sum(Axy*phase_inc_x)+np.sum(Ayy*phase_inc_y)
                    Ez_XZ[j,i]=np.sum(Axz*phase_inc_x)+np.sum(Ayz*phase_inc_y)
        else:
            print('Options for plot_plane are \'X\' and \'Y\' ')
    Ex_XZ*=-1j*focus/Lambda
    Ey_XZ*=1j*focus/Lambda
    Ez_XZ*=1j*focus/Lambda
    
    return Ex_XZ,Ey_XZ,Ez_XZ,Ex_XY,Ey_XY,Ez_XY

