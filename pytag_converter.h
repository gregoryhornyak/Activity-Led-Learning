// pytag_converter.h
// Written by Jozsef Hornyak
// Modified by Leo Head
// A tool used to convert tags into data used by the world generator

#ifndef PYTAG_CONVERTER_H
#define PYTAG_CONVERTER_H

// Include defaults
#include <math.h>

// Convert x and y coords into a single number
int xy_to_i(int x, int y, int width)
{
    return (y*width) + x;
}

// Convert single number to x and y coords
int i_to_xy(int i, bool X0_or_Y1, int width)
{
    int x = i%width;
    int y = i/width;
    if(X0_or_Y1 == 0)
    {
        return x;
    }
    else
    {
        return y;
    }
}

// Return the pythagorean of numbers as an int
int pythagorean(int x, int y)
{
    return sqrt(x*x + y*y);
}

// Return the pythagorean of numbers of an float
float fl_pythagorean(int x, int y)
{
    return sqrt(x*x + y*y);
}

#endif // PYTAG_CONVERTER_H
