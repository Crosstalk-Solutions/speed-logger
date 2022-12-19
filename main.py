import speedtest


def run_test():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()

    results_dict = s.results.dict()
    print(results_dict)
    with open('speedtest.csv', 'a') as f:
        f.write(f"{results_dict['timestamp']}, {results_dict['download']}, {results_dict['upload']}, {results_dict['ping']}\n")


if __name__ == '__main__':
    run_test()
