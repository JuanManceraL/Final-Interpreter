float r1 = 15.0;
float r2 = 10.0;
float h = 25.0;
float M_PI = 3.1415;

float volumen = (M_PI / 3.0) * h * (exp(r1 2) + exp(r2 2) + r1 * r2);

float a = sqr(( exp(h 2)+exp((r1-r2) 2) ));
float area = M_PI * (exp(r1 2) + exp(r2 2) + a * (r1+r2));

printf("Dimensiones del tronco cono:");
printf("Radio mayor (r1):");
printf(r1);
printf("");
printf("Radio menor (r2):");
printf(r2);
printf("");
printf("Altura (h):");
printf(h);
printf("");
printf("Volumen del tronco cono:");
printf(volumen);
printf("");
printf("Área total del tronco cono:");
printf(area);

