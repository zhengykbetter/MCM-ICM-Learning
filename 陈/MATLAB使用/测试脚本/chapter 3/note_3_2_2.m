a = 1:1:12;
b = length(a);
c = a(1);
d = a(1:2:12);
e = a(5:1:end);
a = logspace(1,10,10);

for i = 1:10
    a(i) = mod10to2(a(i));
end

a(1) = 4;
a
a([1,3])=[50,60];
a
a(1:3)=[50,60,70];
a
a(2:4)=100;
a
a(13)=88;
a
a(1)=[];
a
a(end-1:end)=[];
a
a(20) = [];
a