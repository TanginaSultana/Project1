uc_bf=(180+150)*(3/100)
uc_vc=(150+150)*(3/100)
uc_rv=(220+150)*(3/100)
uc_ls=(165+150)*(3/100)
uc_cc=(170+150)*(3/100)

c_bf=uc_bf+180+150+50+60
c_vc=uc_vc+150+150+50+60
c_rv=uc_rv+220+150+50+60
c_ls=uc_ls+165+150+50+60
c_cc=uc_cc+170+150+50+60

p_bf=780-c_bf
p_vc=600-c_vc
p_rv=800-c_rv
p_ls=650-c_ls
p_cc=660-c_cc

bpp_p_bf=(p_bf*100)/c_bf
bpp_p_vc=(p_vc*100)/c_vc
bpp_p_rv=(p_rv*100)/c_rv
bpp_p_ls=(p_ls*100)/c_ls
bpp_p_cc=(p_cc*100)/c_cc

print("Before discount % of Profit:\n")
print("Black Forest = ",bpp_p_bf,"\nVanilla cake = ",bpp_p_vc,"\nRed Velvet = ",bpp_p_rv,"\nLemon Sponge Cake = ",bpp_p_ls,"\nChocolate Cake = ",bpp_p_cc)

print("\n")

bf=780-(780*5)/100
vc=600-(600*5)/100
rv=800-(800*5)/100
ls=650-(650*7)/100
cc=660-(660*7)/100

p_bf=bf-c_bf
p_vc=vc-c_vc
p_rv=rv-c_rv
p_ls=ls-c_ls
p_cc=cc-c_cc

bpp_p_bf=(p_bf*100)/c_bf
bpp_p_vc=(p_vc*100)/c_vc
bpp_p_rv=(p_rv*100)/c_rv
bpp_p_ls=(p_ls*100)/c_ls
bpp_p_cc=(p_cc*100)/c_cc

print("After discount % of Profit:\n")
print("Black Forest = ",bpp_p_bf,"\nVanilla cake = ",bpp_p_vc,"\nRed Velvet = ",bpp_p_rv,"\nLemon Sponge Cake = ",bpp_p_ls,"\nChocolate Cake = ",bpp_p_cc)



