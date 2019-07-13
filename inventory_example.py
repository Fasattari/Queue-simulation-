from scheduler_class import *

demand_list=[40,50,60,70,80,90,100]
prob_demand_list=[[0.03,0.05,0.15,0.20,0.35,0.15,0.07],[0.1,0.18,0.40,0.20,0.08,0.04,0],[0.44,0.22,0.16,0.12,0.06,0,0]]
day_list=["good","fair","poor"]
day_probs=[0.35,0.45,0.2]
inv = Inventory(70,1,70,33,5)
inv.set_priority_demad(demand_list, prob_demand_list, day_list, day_probs)
print inv.get_demand_num()
print inv.get_demand_num()
print inv.get_demand_num()
print inv.get_demand_num()
env = Environment()
env.add_inventory(inv)
env.set_stop(880)
scheduler = Scheduler(env,day=40)
scheduler.start()
