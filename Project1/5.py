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

t_p_bf=p_bf*5
t_p_vc=p_vc*7
t_p_rv=p_rv*10
t_p_ls=p_ls*5
t_p_cc=p_cc*9
print("Black Forest = ",t_p_bf,"\nVanilla cake = ",t_p_vc,"\nRed Velvet = ",t_p_rv,"\nLemon Sponge Cake = ",t_p_ls,"\nChocolate Cake = ",t_p_cc)
