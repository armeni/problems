s = 3;
n = 5;
x = linspace(-1, 1);
xi = linspace(-1, 1, n);

f = x - sin(x);
hold on
figure(1);
plot(x, f)

y = zeros(n, 1);
for i = 1:n
y(i,1) = xi(i) - sin(xi(i));
end

Q = zeros(n, s);

for i = 1:n
    for j = 1:s+1
        Q(i,j) = xi(i)^(j-1);
    end
end

H = Q' * Q;
B = Q' * y;
a = H \ B;

syms x;
P = a(1) * x^0;

for i = 2:s+1
    P = P + a(i) * x^(i-1);
end

collect(P);
Polynom = vpa(P, 6)
hold on
p = ezplot(Polynom, [-1, 1]);
set(p);