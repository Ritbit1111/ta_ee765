import pandas as pd
import numpy as np
from bokeh.layouts import row, column, gridplot
from bokeh.embed import server_document
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import Figure, ColumnDataSource
from bokeh.server.server import Server

def get_weibull(a , lmbda = 1,  k = 1000):
    np.random.seed(2)
    s = np.random.weibull(a, k)
    hist, edges = np.histogram(lmbda*s, density=True, bins=2500)
    left_edges = edges[:-1]
    right_edges = edges[1:]
    return dict(hist = hist, left_edges = left_edges, right_edges = right_edges)

def get_normal(mu = 0, sigma = 1, k = 1000):
    #np.random.seed(2)
    s = np.random.normal(mu, sigma, k)
    hist, edges = np.histogram(s, density=True, bins=1000)
    left_edges = edges[:-1]
    right_edges = edges[1:]
    return dict(hist = hist, left_edges = left_edges, right_edges = right_edges)

def get_exponential(scale , k = 1000):
   #np.random.seed(2)
    s = np.random.exponential(scale , k)
    hist, edges = np.histogram(s, density=True, bins=1000)
    left_edges = edges[:-1]
    right_edges = edges[1:]
    return dict(hist = hist, left_edges = left_edges, right_edges = right_edges)

def get_lognormal(mu = 1, sigma=1 , k = 1000):
   #np.random.seed(2)
    s = np.random.lognormal(mu, sigma , k)
    #np.log(s) will be normally distributed
    hist, edges = np.histogram(s, density=True, bins=2500)
    left_edges = edges[:-1]
    right_edges = edges[1:]
    return dict(hist = hist, left_edges = left_edges, right_edges = right_edges)


def plot(width, height):
######################################################################################################################
    source_normal = ColumnDataSource(data = get_normal(0,1,10000))
    plot_normal = Figure(plot_width = width, plot_height = height, x_range = (-6,6), title = 'Normal')
    plot_normal.quad(top='hist', bottom=0, left='left_edges', right='right_edges',
                     source= source_normal, fill_color="navy")
    
    def update_plot_normal(attrname, old , new):
        source_normal.data = get_normal(mu_slider.value, sigma_slider.value, 100000)
    
    mu_slider = Slider(start = -5, end = 5, value = 0, step = 0.2, title = 'Mean')
    mu_slider.on_change('value', update_plot_normal)
    
    sigma_slider = Slider(start = 0.1, end = 5, value = 1, step = 0.2, title = 'Std_Dev')
    sigma_slider.on_change('value', update_plot_normal)

######################################################################################################################
    source_weibull = ColumnDataSource(data = get_weibull(1.5, 1, 10000))
    plot_weibull = Figure(plot_width = width, plot_height = height, x_range = (0,6), title = 'Weibull')
    plot_weibull.quad(top='hist', bottom=0, left='left_edges', right='right_edges', 
                      source= source_weibull, fill_color="navy")
    
    def update_plot_weibull(attrname, old , new):
        source_weibull.data = get_weibull(shape_slider.value,lambda_slider.value,100000)
    
    shape_slider = Slider(start = 0.4, end = 5, value = 1.5, step = 0.1, title = 'Shape a')
    shape_slider.on_change('value', update_plot_weibull)
    
    lambda_slider = Slider(start = 0.5, end = 3, value = 1, step = 0.5, title = 'Lambda')
    lambda_slider.on_change('value', update_plot_weibull)
    
######################################################################################################################
    source_lognormal = ColumnDataSource(data = get_lognormal(0.9, 0.16, 10000))
    plot_lognormal = Figure(plot_width = width, plot_height = height, title = 'Lognormal', 
                            y_range=(0,2), x_range = (0,10))
    plot_lognormal.quad(top='hist', bottom=0, left='left_edges', right='right_edges', 
                        source= source_lognormal, fill_color="navy")
    
    def update_plot_lognormal(attrname, old , new):
        source_lognormal.data = get_lognormal(mean_slider_lognormal.value, sigma_slider_lognormal.value,100000)
    
    mean_slider_lognormal = Slider(start = 0, end = 5, value =0.9, step = 0.1, title = 'Mean')
    mean_slider_lognormal.on_change('value', update_plot_lognormal)
    
    sigma_slider_lognormal = Slider(start = 0.01, end = 1, value = 0.16, step = 0.01, title = 'Std_dev')
    sigma_slider_lognormal.on_change('value', update_plot_lognormal)
######################################################################################################################
    source_exponential = ColumnDataSource(data = get_exponential(3, 1000))
    plot_exponential = Figure(plot_width = width, plot_height = height, title = 'Exponential',
                              x_range=(0,50), y_range =(0,1) )
    plot_exponential.quad(top='hist', bottom=0, left='left_edges', right='right_edges', 
                          source= source_exponential, fill_color="green")
    
    def update_plot_exponential(attrname, old , new):
        source_exponential.data = get_exponential(scale_slider_exponential.value, 10000)
    
    scale_slider_exponential = Slider(start = 0.1, end = 10, value = 3, step = 0.1, title = 'Scale')
    scale_slider_exponential.on_change('value', update_plot_exponential)

    layout1 = column(plot_normal, column(mu_slider, sigma_slider))
    layout2 = column(plot_weibull, column(shape_slider, lambda_slider))
    layout3 = column(plot_lognormal, column(mean_slider_lognormal, sigma_slider_lognormal))
    layout4 = column(plot_exponential, scale_slider_exponential)
    top = row(layout1, layout2)
    bottom = row(layout3, layout4)
    return (row(top, bottom))

