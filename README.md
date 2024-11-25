<div align="center">

# `fossiler` : a suite tool of fossil calibration finding
**Hengchi Chen**

[**Bioinformatics & Evolutionary Genomics Group**](https://www.vandepeerlab.be/)**, VIB-UGent Center for Plant Systems Biology**

[**Installation**](#installation) |
[**Parameters**](#parameters) |
[**Usage**](#usage) |
</div>

## Installation
The `fossiler` package can be readily installed via `PYPI`. An example command is given below.

```
virtualenv -p=python3 ENV (or python3/python -m venv ENV)
source ENV/bin/activate
pip install fossiler
```

Note that if users want to get the latest update, it's suggested to install from the source because the update on `PYPI` will be later than here of source. To install from source, the following command can be used.

```
git clone https://github.com/heche-psb/fossiler
cd fossiler
virtualenv -p=python3 ENV (or python3 -m venv ENV)
source ENV/bin/activate
pip install -r requirements.txt
pip install .
```

If there is permission problem in the installation, please try the following command.

```
pip install -e .
```

## Parameters
The implemented parameters are as below.

```
fossiler find
--------------------------------------------------------------------------------
-t, --tree, the tree topology file to assign fossil calibrations, default None
-mf, --mcmctreeformat, flag option, whether to get mcmctree format output
-wt, --wholetree, flag option, whether to use the whole angiosperm tree infomation instead of only user-defined local tree
-sc, --setconserved, flag option, whether to adopt the same maximum constraint as in Morris et al. (2018)
-gs, --getsp, flag option, whether to get species in the starting tree
-oo, --onlyone, flag option, whether to get only one species per order
-ut, --updatedtree, flag option, whether to use updated angiosperm phylogeny from our paper instead of APG IV
-cb, --combined, flag option, whether to use fossil calibrations based on combined database
-gt, --getaxonomy, get taxonomy information of a given species name, default None
-e, --email, email address to make requests to NCBI's Entrez utilities, default None
```

## Usage
Below we give an example of using `fossiler` to obtain fossil calibrations.

```
fossiler find -mf -wt -sc -gs -ut -t inputfile
```

The `inputfile` is a tree file documenting the species names or taxonomy names. An example is as follows.

```
9 1
(((Alismatales,(Pandanales,Dioscoreales)),Acorales),(((Trochodendrales,Buxales),Proteales),(Aquilegia_coerulea_ap1,Aquilegia_coerulea_ap2)));
```

Species names should be joined by underlines. Note that it's allowed to append `_ap1` and `_ap2` at the end of a species name to create the starting tree file for WGD dating using `wgd v2`.

There will be 5 output files as below.

```
--inputfile.addtime
9 1
(((Alismatales,(Pandanales,Dioscoreales)'>0.5600<1.2863')'>0.8360<1.2863',Acorales)'>0.8360<1.2863',(((Trochodendrales,Buxales)'>1.1080<1.2863',Proteales)'>1.1080<1.2863',(Aquilegia_coerulea_ap1,Aquilegia_coerulea_ap2))'>1.1080<1.2863')'>1.2720<2.4720';

--inputfile.addtime_17sp
17 1
((((Potamogeton_acutifolius,(Spirodela_intermedia,Amorphophallus_konjac)),(Acanthochlamys_bracteata,(Dioscorea_alata,Dioscorea_rotundata))'>0.5600<1.2863')'>0.8360<1.2863',(Acorus_americanus,Acorus_tatarinowii))'>0.8360<1.2863',((((Tetracentron_sinense,Trochodendron_aralioides),(Buxus_austroyunnanensis,Buxus_sinica))'>1.1080<1.2863',(Nelumbo_nucifera,(Telopea_speciosissima,Protea_cynaroides)))'>1.1080<1.2863',(Aquilegia_coerulea_ap1,Aquilegia_coerulea_ap2))'>1.1080<1.2863')'>1.2720<2.4720';

--inputfile.addtime_sp17_species_list_lines
Potamogeton_acutifolius
Spirodela_intermedia
Amorphophallus_konjac
Acanthochlamys_bracteata
Dioscorea_alata
Dioscorea_rotundata
Acorus_americanus
Acorus_tatarinowii
Tetracentron_sinense
Trochodendron_aralioides
Buxus_austroyunnanensis
Buxus_sinica
Nelumbo_nucifera
Telopea_speciosissima
Protea_cynaroides

--inputfile.addtime_sp17_species_list_space
Potamogeton_acutifolius Spirodela_intermedia Amorphophallus_konjac Acanthochlamys_bracteata Dioscorea_alata Dioscorea_rotundata Acorus_americanus Acorus_tatarinowii Tetracentron_sinense Trochodendron_aralioides Buxus_austroyunnanensis Buxus_sinica Nelumbo_nucifera Telopea_speciosissima Protea_cynaroides Aquilegia_coerulea

--inputfile.addtime_taxonomy
9 1
(((Alismatales,(Pandanales,Dioscoreales)'>0.5600<1.2863')'>0.8360<1.2863',Acorales)'>0.8360<1.2863',(((Trochodendrales,Buxales)'>1.1080<1.2863',Proteales)'>1.1080<1.2863',(Ranunculales,Ranunculales))'>1.1080<1.2863')'>1.2720<2.4720';
```
The output file with suffix of 'addtime' is the tree file with fossil calibrations assigned on internal nodes. The output file with suffix of 'addtime_17sp' is the tree file with taxonomy represented in species and fossil calibrations assigned on internal nodes. The output file with suffix of 'addtime_sp17_species_list_lines' is the file documenting the species information line by line. The output file with suffix of 'addtime_sp17_species_list_space' is the file documenting the species information in one line separated by space. The output file with suffix of 'addtime_taxonomy' is the tree file with taxonomy represented in order and fossil calibrations assigned on internal nodes.

