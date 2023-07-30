from . import NetworkDelay


def test_network_delay_time_1(capsys):
    with capsys.disabled():
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        params = (times, n, k)
        expected = 2
        instance = NetworkDelay()
        response = instance.networkDelayTime(*params)

        assert expected == response


# def test_network_delay_time_2(capsys):
#     with capsys.disabled():
#         times = [[1, 2, 1]]
#         n = 2
#         k = 1
#         params = [times, n, k]
#         expected = 1
#         instance = NetworkDelay()
#         response = instance.networkDelayTime(*params)

#         assert expected == response
