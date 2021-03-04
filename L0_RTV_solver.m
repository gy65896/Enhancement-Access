function Smg = L0_RTV_solver(Img, opts);

[D,Dt]  = defDDt;
%
lambdaU = 2 * opts.lambda0 ./ opts.beta;
lambdaS = 2 * opts.lambda1 * opts.ptime;

Umgx = Img;
Umgy = Img;

Smgb = Img;
Smg  = Img;
%
for ii = 1:opts.MaxOuter
    %
    for kk = 1:size(Img,3)
        [DxSmg(:,:,kk), DySmg(:,:,kk)]   = D(squeeze(Smg(:,:,kk)));
    end

    Umgx = L0Smoothing(DxSmg, lambdaU);
    Umgy = L0Smoothing(DySmg, lambdaU);
    %
    for jj = 1:opts.MaxIterS
        %
        % Sbar-Subproblem
        for kk = 1:size(Img,3)
            Sterm(:,:,kk) = Dt(DxSmg(:,:,kk) - Umgx(:,:,kk), DySmg(:,:,kk) - Umgy(:,:,kk));
            Smgb(:,:,kk)  = Smgb(:,:,kk) - opts.ptime * (Smg(:,:,kk) - Img(:,:,kk) + opts.beta * Sterm(:,:,kk));
        end
        % S-Subproblem
        Smg = tsmooth(Smgb,lambdaS,3);
        %
    end
end

    function C = getC
        %
        sizeF     = size(Ia);
        % psf2otf ——computes the Fast Fourier Transform (FFT) of the point-spread function (PSF)
        C.eigsD1  = psf2otf([1,-1], sizeF);  %▽x
        C.eigsD2  = psf2otf([1;-1], sizeF);  %▽y
        C.eigsDtD = abs(C.eigsD1).^2 + abs(C.eigsD2).^2; %▽t*▽
        %
    end
%
    function [D,Dt] = defDDt
        % defines finite difference operator D %有限差分运算▽
        % and its transpose operator           %▽的转置运算
        % referring to FTVD code
        D = @(U) ForwardD(U);
        Dt = @(X,Y) Dive(X,Y);
    end
%
    function [Dux,Duy] = ForwardD(U) %diff      %有限差分运算▽
        % Forward finite difference operator
        Dux = [diff(U,1,2), U(:,1) - U(:,end)];
        Duy = [diff(U,1,1); U(1,:) - U(end,:)];
    end
%
    function DtXY = Dive(X,Y) %Dt=-div        %▽的转置运算
        % Transpose of the forward finite difference operator
        DtXY = [X(:,end) - X(:, 1), -diff(X,1,2)];
        DtXY = DtXY + [Y(end,:) - Y(1, :); -diff(Y,1,1)];
    end
%

end