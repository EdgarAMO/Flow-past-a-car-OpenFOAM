// depth is in the 'z' direction:

// car is:
//  4.0[m] long
//  1.5[m] wide
//  1.5[m] high

long = 4.5;
wide = 1.5;
high = 1.5;

translate([0, 0, high/2])
    rotate([-90, 0, 0])
        resize([long, wide, high])
            import("car.stl");

