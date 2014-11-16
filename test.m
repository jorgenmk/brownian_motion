broken = 0;

kast = 100000;
itertions = 10000;
range = 1;

mean_end = 0;
mean_downers = 0;

for i = 0:kast
    [sim,broke] = calc(iterations, range);
    %plot(sim);
    if broke == 1
        broken = broken + 1;
        mean_downers = mean_downers + sim(iterations);
    else
        mean_end = mean_end + sim(iterations);
    end
end

X = sprintf('Mean not broken: %s\nMean broken: %s\nBroken: %s\nBroken: %s%%\nTotal mean: %s', num2str(mean_end/(kast-broken)), num2str(mean_downers/broken), num2str(broken), num2str((broken/kast)*100), num2str((mean_end+mean_downers)/kast));
disp(X)
%disp(mean_end/(iterations-broken));
%disp(mean_downers/broken);
%disp((mean_end+mean_downers)/iterations);
%disp(broken);
%disp((broken/iterations)*100);

