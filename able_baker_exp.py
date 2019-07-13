from scheduler_class import *


def able_baker():
    dis_server = Distribution()
    line = Line()
    able_server = Server(dis_server, line)
    baker_server = Server(dis_server, line)
    ph = Phase()
    ph.addServer(able_server, 0.9)
    ph.addServer(baker_server, 0.1)
    ph.set_probability()

    create_dis = Distribution('gamma',[2,7])
    create = Create(create_dis, num_entity=100)
    env = Environment(create)
    env.add_phase(ph)


    sch = Scheduler(env)
    sch.start()
    st = sch.get_statistics()
    st.sort_entity()
    st.plot_num_entity_time()
    st.plot_server([able_server, baker_server], ['able_server', ' baker_server'])
    st.plot_server_utilization([able_server, baker_server],  ['able_server', 'baker_server'])

able_baker()
