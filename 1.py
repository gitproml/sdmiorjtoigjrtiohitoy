for i in range(1,49):
    key1 = 'douyinzhibo%02d'%i
    keyy = '{}xby'.format(key1)
    # cmd = 'git checkout {}'.format(keyy)
    cmd = 'mkdir {} && echo "FROM muyangren907/dyzb:{}" > {}/Dockerfile'.format(keyy,keyy,keyy)
    # cmd += '&& docker build . -t muyangren907/dyzb:{} && docker push muyangren907/dyzb:{}'.format(keyy,keyy)

    
    print(cmd)

for i in range(1,49):
    key1 = 'douyinzhibo%02d'%i
    keyy = '{}sby'.format(key1)
    cmd = 'mkdir {} && echo "FROM muyangren907/dyzb:{}" > {}/Dockerfile'.format(keyy,keyy,keyy)
    print(cmd)

for i in range(1,23):
    key1 = 'dymcmn%02d'%i
    keyy = '{}sby'.format(key1)
    cmd = 'mkdir {} && echo "FROM muyangren907/dyzb:{}" > {}/Dockerfile'.format(keyy,keyy,keyy)
    
    print(cmd)

for i in range(1,23):
    key1 = 'dymcmn%02d'%i
    keyy = '{}xby'.format(key1)
    cmd = 'mkdir {} && echo "FROM muyangren907/dyzb:{}" > {}/Dockerfile'.format(keyy,keyy,keyy)
    
    print(cmd)