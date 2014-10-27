broken = 0;

for i = 0:1000
    [sim,broke] = calc();
    %plot(sim);
    if broke == 1
        broken = broken + 1;
    end
end

disp(broken)



