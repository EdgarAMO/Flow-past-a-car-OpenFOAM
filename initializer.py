# calculate l, nut, epsilon, omega:

import sys

if __name__ == '__main__':
	u  = float(sys.argv[1])

	# turbulent length scale is based on a wake: 0.08L, where L is the wake's width

	ls = 0.08 * 2                               	# characteristic length is 2[m]
	k = 1.5 * (u * 0.05) ** 2                   	# turbulent kinetic energy
	epsilon = pow(0.09, 0.75) * pow(k, 1.5) / ls    # epsilon
	omega = pow(k, 0.5) / (pow(0.09, 0.25) * ls)	# omega
	nut = 0.09 * pow(k, 2) / epsilon                # nut
	
	file = open('constants', 'w')
	file.write('U\t{0:9.6f};\n'.format(u))
	file.write('k\t{0:9.6f};\n'.format(k))
	file.write('epsilon\t{0:9.6f};\n'.format(epsilon))
	file.write('omega\t{0:9.6f};\n'.format(omega))
	file.write('nut\t{0:9.6f};'.format(nut))
	
	file.close()
