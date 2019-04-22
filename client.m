close all;clear all;clc;
ip=input('Please input the server IP addres and  port.\n','s');
port=input('');
tcpipClient = tcpip(ip,port,'NetworkRole','Client');
set(tcpipClient,'InputBufferSize',4500000);
fopen(tcpipClient);
rawData = fread(tcpipClient,1024,'char')';
disp(native2unicode(rawData))
goal=input('What dou you want?\n(word/picture/music)\n','s');
if strcmp(goal,'word')
    fwrite(tcpipClient,'word','char');
    rawData1=fread(tcpipClient,4500000,'char')';
    disp(native2unicode(rawData1));
elseif strcmp(goal,'picture')
    fwrite(tcpipClient,'picture','char');
    rawData2=fread(tcpipClient,4500000,'char')';
    n=1;
    im=nan(200,200,3);
    for i=1:200
        for j=1:200
            for k=1:3
                im(i,j,k)=rawData2(n);
                n=n+1;
            end
        end
    end
    imshow(uint8(im));
elseif strcmp(goal,'music')
    fwrite(tcpipClient,'music','char');
    rawData3=fread(tcpipClient,4500000,'char')';
    [fid,message]=fopen('new.wav','wb');
    fwrite(fid,rawData3);
    [y,f]=audioread('new.wav');
    fclose(fid);
    sound(y,f);
end
fclose(tcpipClient);
