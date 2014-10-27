function [sim, broke] = calc()

st = 100.0;
my = 0.045;
iterations = 1000;
sigma = 0.3;
delta_t = 1/iterations;
barrier = 65;
broke = 0;

st_start = st;
sim = zeros(iterations);

for i = 1:iterations
    st_start = st_start*exp((my-0.5*sigma^2)*delta_t+sigma*randn()*sqrt(delta_t));
    sim(i) = st_start;
    if st_start <= barrier
        broke = 1;
    end
end
end

