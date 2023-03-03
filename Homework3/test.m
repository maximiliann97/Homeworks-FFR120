clear all
clc

sum_of_credits = 180;

python = 7.5*3;
intro_ai = 7.5*4;
bachelor = 15*5;
regler = 7.5*5;
vp = 7.5*4;
dynkan = 7.5*3;
material = 7.5*5;
mekatronik = 7.5*3;
fluid = 7.5*4;
statistik = 4*4;
indek = 7.5*4;
sustain = 3.5*5;
termo = 7.5*4;
ikot = 7.5*5;
tillverk = 7.5*4;
maskinelem = 7.5*5;
hallf = 7.5*3;
flervarre = 7.5*3;
linj = 7.5*3;
staten = 7.5*3;
cad = 4*4;
envarre = 7.5*3;
metodik = 7.5*4;
intromatte = 7.5*4;
matlab = 7.5*4;
data = 7.5*5;
logi = 7.5*5;

w = (intro_ai + bachelor + regler + vp + material + mekatronik + fluid + statistik + indek + sustain + termo + ikot + tillverk + maskinelem + hallf + ...
    flervarre + linj + staten + cad + envarre + metodik + intromatte + matlab + data + logi);

weight = w/sum_of_credits