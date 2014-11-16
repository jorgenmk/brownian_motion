function [sim, broke] = calc(iterations, range)

st = 100.0;
my = 0.045;
barrier = 65;
sigma = 0.3;

delta_t = (1/iterations)*range;

broke = 0;

st_start = st;
sim = zeros(1,iterations);
randoms = randn(1,iterations);

%disp "Mean:", mean(randoms)

for i = 1:iterations
    st_start = st_start*exp((my-0.5*sigma^2)*delta_t+sigma*randoms(i)*sqrt(delta_t));
    sim(i) = st_start;
    if st_start <= barrier
        broke = 1;
    end
end
end

