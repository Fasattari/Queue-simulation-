from scheduler_class import *


def main():
    dis_server = Distribution()
    line = Line(5)
    server = Server(dis_server, line)
    line2 = Line(4)
    ser2 = Server(dis_server, line2)
    ph = Phase()
    ph.addServer(server, 0.3)
    ph.addServer(ser2, 0.7)
    ph.set_probability()

    server_dist = Distribution('gamma', [4, 2])
    line3 = Line(9)
    ser3 = Server(server_dist, line3)
    line4 = Line(10)
    ser4 = Server(server_dist, line4)
    ph2 = Phase()
    ph2.addServer(ser3, 0.5)
    ph2.addServer(ser4, 0.5)
    ph2.set_probability()

    create_dis = Distribution('normal', [5, 0.1])
    create = Create(create_dis)
    env = Environment(create)
    env.add_phase(ph)
    env.add_phase(ph2)
    env.set_stop(30)
    sch = Scheduler(env)
    sch.start()
    in_list = sch.get_output()
    st = sch.get_statistics()

    create2 = Create(create_dis, in_list,5)
    env2 = Environment(create2)
    env2.add_phase(ph)
    env2.add_phase(ph2)
    env2.set_stop(30)
    sch2 = Scheduler(env2, in_list[0][0],st)
    sch2.start()
    sch2.get_statistics().sort_entity()

    num = 5
    #print "probaility of "+ num + "entity in system :",sch2.get_statistics().get_p_n(num)
    print "w_n :",sch2.get_statistics().get_w_n(3)
    print "l_t :",sch2.get_statistics().get_l_t(3)
    sch2.get_statistics().plot_num_entity_time()
    st.plot_server([server, ser2, ser3, ser4], ['server_1', 'server_2', 'server_3', 'server_4'])
main()

