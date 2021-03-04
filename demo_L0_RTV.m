function Y = demo_L0_RTV(X)

opts.lambda0 = 3;
opts.lambda1 = 1;
opts.beta  = 1;
opts.ptime = 0.5;
opts.MaxOuter = 2;
opts.MaxIterS = 2;

Y = L0_RTV_solver(X, opts);
end


