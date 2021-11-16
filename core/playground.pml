load /Users/albertdarmawan/Documents/gass-ppi/pymol/1ahw.pdb;
load /Users/albertdarmawan/Documents/gass-ppi/pymol/1fgn.pdb;
load /Users/albertdarmawan/Documents/gass-ppi/pymol/1tfh.pdb;
load /Users/albertdarmawan/Documents/gass-ppi/dataset/benchmark5/structures/1AHW_l_u.pdb;
load /Users/albertdarmawan/Documents/gass-ppi/dataset/benchmark5/structures/1AHW_r_u.pdb;
load /Users/albertdarmawan/Documents/gass-ppi/dataset/benchmark5/structures/1AHW_l_b.pdb;
load /Users/albertdarmawan/Documents/gass-ppi/dataset/benchmark5/structures/1AHW_r_b.pdb;

set ray_opaque_background, off
set ray_shadows,off;

ray;
png 1ahw.png;

set cartoon_transparency, 0.5, 1ahw
ray;
png 1ahw-interface.png;

load /Users/albertdarmawan/Documents/gass-ppi/core/3nos_new.pdb