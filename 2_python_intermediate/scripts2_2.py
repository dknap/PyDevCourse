import time, os, sys, argparse

# path_from = sys.argv[1]

def readFromFile(*path_to_files):
    if path_to_files is not None:
        for path in path_to_files:
            server_file = open(path, 'r')
            server_configuration = server_file.read()
        print(server_configuration)
        server_file.close()

def writeToFile(*path_to_files):
    if path_to_files is not None:
        for path in path_to_files:
            server_file = open(path, 'w')
            title = 'Developer Mode\n'
            server_file.write(title)
            server_params = ['CPU=20\n', 'RAM=30G\n']
            server_file.write(''.join(server_params))
            server_file.close()

try:
    path_from = sys.argv[1]
except:
    print('Sys argument error :(')

stage = os.getenv('STAGE', default='dev').upper()
if stage.startswith('PROD'):
    output = f'SERVER is in {stage} mode'
    print(output)
    exit()
elif os.path.exists(path_from):
    readFromFile(path_from)
else:
    writeToFile(path_from)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', dest='path_from', default='./server.conf', help='Path to your file')
    results = parser.parse_args()
    start_time = time.localtime()
    print('Script start time: {}:{}:{} '.format(start_time.tm_hour, start_time.tm_min, start_time.tm_sec))
    # h =  time.localtime().tm_zone
    # print(h)

    time.sleep(1)
    stop_time = time.localtime()
    print('Script stopped at: {} '.format(time.strftime('%X', stop_time)))

    difference = time.mktime(stop_time) - time.mktime(start_time)
    print('Total time: {} seconds'.format(difference))

if __name__ == '__main__':
    main()