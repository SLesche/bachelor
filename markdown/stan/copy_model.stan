// generated with brms 2.18.0
functions {
  /* Wiener diffusion log-PDF for a single response
   * Args:
   *   y: reaction time data
   *   dec: decision data (0 or 1)
   *   alpha: boundary separation parameter > 0
   *   tau: non-decision time parameter > 0
   *   beta: initial bias parameter in [0, 1]
   *   delta: drift rate parameter
   * Returns:
   *   a scalar to be added to the log posterior
   */
   real wiener_diffusion_lpdf(real y, int dec, real alpha,
                              real tau, real beta, real delta) {
     if (dec == 1) {
       return wiener_lpdf(y | alpha, tau, beta, delta);
     } else {
       return wiener_lpdf(y | alpha, tau, 1 - beta, - delta);
     }
   }
}
data {
  int<lower=1> N;  // total number of observations
  vector[N] Y;  // response variable
  int<lower=0,upper=1> dec[N];  // decisions
  int<lower=1> K;  // number of population-level effects
  matrix[N, K] X;  // population-level design matrix
  int<lower=1> K_bs;  // number of population-level effects
  matrix[N, K_bs] X_bs;  // population-level design matrix
  int<lower=1> K_ndt;  // number of population-level effects
  matrix[N, K_ndt] X_ndt;  // population-level design matrix
  int<lower=1> K_bias;  // number of population-level effects
  matrix[N, K_bias] X_bias;  // population-level design matrix
  // data for group-level effects of ID 1
  int<lower=1> N_1;  // number of grouping levels
  int<lower=1> M_1;  // number of coefficients per level
  int<lower=1> J_1[N];  // grouping indicator per observation
  // group-level predictor values
  vector[N] Z_1_1;
  vector[N] Z_1_2;
  vector[N] Z_1_3;
  vector[N] Z_1_4;
  vector[N] Z_1_5;
  vector[N] Z_1_6;
  vector[N] Z_1_7;
  vector[N] Z_1_8;
  vector[N] Z_1_9;
  vector[N] Z_1_10;
  vector[N] Z_1_11;
  vector[N] Z_1_12;
  vector[N] Z_1_13;
  vector[N] Z_1_14;
  vector[N] Z_1_15;
  vector[N] Z_1_16;
  vector[N] Z_1_17;
  vector[N] Z_1_18;
  vector[N] Z_1_19;
  vector[N] Z_1_20;
  vector[N] Z_1_21;
  vector[N] Z_1_22;
  vector[N] Z_1_23;
  vector[N] Z_1_24;
  // data for group-level effects of ID 2
  int<lower=1> N_2;  // number of grouping levels
  int<lower=1> M_2;  // number of coefficients per level
  int<lower=1> J_2[N];  // grouping indicator per observation
  // group-level predictor values
  vector[N] Z_2_bs_1;
  vector[N] Z_2_bs_2;
  vector[N] Z_2_bs_3;
  vector[N] Z_2_bs_4;
  vector[N] Z_2_bs_5;
  vector[N] Z_2_bs_6;
  vector[N] Z_2_bs_7;
  vector[N] Z_2_bs_8;
  vector[N] Z_2_bs_9;
  vector[N] Z_2_bs_10;
  vector[N] Z_2_bs_11;
  vector[N] Z_2_bs_12;
  // data for group-level effects of ID 3
  int<lower=1> N_3;  // number of grouping levels
  int<lower=1> M_3;  // number of coefficients per level
  int<lower=1> J_3[N];  // grouping indicator per observation
  // group-level predictor values
  vector[N] Z_3_ndt_1;
  vector[N] Z_3_ndt_2;
  vector[N] Z_3_ndt_3;
  vector[N] Z_3_ndt_4;
  vector[N] Z_3_ndt_5;
  vector[N] Z_3_ndt_6;
  vector[N] Z_3_ndt_7;
  vector[N] Z_3_ndt_8;
  vector[N] Z_3_ndt_9;
  vector[N] Z_3_ndt_10;
  vector[N] Z_3_ndt_11;
  vector[N] Z_3_ndt_12;
  // data for group-level effects of ID 4
  int<lower=1> N_4;  // number of grouping levels
  int<lower=1> M_4;  // number of coefficients per level
  int<lower=1> J_4[N];  // grouping indicator per observation
  // group-level predictor values
  vector[N] Z_4_bias_1;
  vector[N] Z_4_bias_2;
  vector[N] Z_4_bias_3;
  vector[N] Z_4_bias_4;
  vector[N] Z_4_bias_5;
  vector[N] Z_4_bias_6;
  vector[N] Z_4_bias_7;
  vector[N] Z_4_bias_8;
  vector[N] Z_4_bias_9;
  vector[N] Z_4_bias_10;
  vector[N] Z_4_bias_11;
  vector[N] Z_4_bias_12;
  int prior_only;  // should the likelihood be ignored?
}
transformed data {
  real min_Y = min(Y);
}
parameters {
  vector[K] b;  // population-level effects
  vector<lower=0>[K_bs] b_bs;  // population-level effects
  vector<lower=0,upper=0.15>[K_ndt] b_ndt;  // population-level effects
  vector<lower=0,upper=1>[K_bias] b_bias;  // population-level effects
  vector<lower=0>[M_1] sd_1;  // group-level standard deviations
  vector[N_1] z_1[M_1];  // standardized group-level effects
  vector<lower=0>[M_2] sd_2;  // group-level standard deviations
  vector[N_2] z_2[M_2];  // standardized group-level effects
  vector<lower=0>[M_3] sd_3;  // group-level standard deviations
  vector[N_3] z_3[M_3];  // standardized group-level effects
  vector<lower=0>[M_4] sd_4;  // group-level standard deviations
  vector[N_4] z_4[M_4];  // standardized group-level effects
}
transformed parameters {
  vector[N_1] r_1_1;  // actual group-level effects
  vector[N_1] r_1_2;  // actual group-level effects
  vector[N_1] r_1_3;  // actual group-level effects
  vector[N_1] r_1_4;  // actual group-level effects
  vector[N_1] r_1_5;  // actual group-level effects
  vector[N_1] r_1_6;  // actual group-level effects
  vector[N_1] r_1_7;  // actual group-level effects
  vector[N_1] r_1_8;  // actual group-level effects
  vector[N_1] r_1_9;  // actual group-level effects
  vector[N_1] r_1_10;  // actual group-level effects
  vector[N_1] r_1_11;  // actual group-level effects
  vector[N_1] r_1_12;  // actual group-level effects
  vector[N_1] r_1_13;  // actual group-level effects
  vector[N_1] r_1_14;  // actual group-level effects
  vector[N_1] r_1_15;  // actual group-level effects
  vector[N_1] r_1_16;  // actual group-level effects
  vector[N_1] r_1_17;  // actual group-level effects
  vector[N_1] r_1_18;  // actual group-level effects
  vector[N_1] r_1_19;  // actual group-level effects
  vector[N_1] r_1_20;  // actual group-level effects
  vector[N_1] r_1_21;  // actual group-level effects
  vector[N_1] r_1_22;  // actual group-level effects
  vector[N_1] r_1_23;  // actual group-level effects
  vector[N_1] r_1_24;  // actual group-level effects
  vector[N_2] r_2_bs_1;  // actual group-level effects
  vector[N_2] r_2_bs_2;  // actual group-level effects
  vector[N_2] r_2_bs_3;  // actual group-level effects
  vector[N_2] r_2_bs_4;  // actual group-level effects
  vector[N_2] r_2_bs_5;  // actual group-level effects
  vector[N_2] r_2_bs_6;  // actual group-level effects
  vector[N_2] r_2_bs_7;  // actual group-level effects
  vector[N_2] r_2_bs_8;  // actual group-level effects
  vector[N_2] r_2_bs_9;  // actual group-level effects
  vector[N_2] r_2_bs_10;  // actual group-level effects
  vector[N_2] r_2_bs_11;  // actual group-level effects
  vector[N_2] r_2_bs_12;  // actual group-level effects
  vector[N_3] r_3_ndt_1;  // actual group-level effects
  vector[N_3] r_3_ndt_2;  // actual group-level effects
  vector[N_3] r_3_ndt_3;  // actual group-level effects
  vector[N_3] r_3_ndt_4;  // actual group-level effects
  vector[N_3] r_3_ndt_5;  // actual group-level effects
  vector[N_3] r_3_ndt_6;  // actual group-level effects
  vector[N_3] r_3_ndt_7;  // actual group-level effects
  vector[N_3] r_3_ndt_8;  // actual group-level effects
  vector[N_3] r_3_ndt_9;  // actual group-level effects
  vector[N_3] r_3_ndt_10;  // actual group-level effects
  vector[N_3] r_3_ndt_11;  // actual group-level effects
  vector[N_3] r_3_ndt_12;  // actual group-level effects
  vector[N_4] r_4_bias_1;  // actual group-level effects
  vector[N_4] r_4_bias_2;  // actual group-level effects
  vector[N_4] r_4_bias_3;  // actual group-level effects
  vector[N_4] r_4_bias_4;  // actual group-level effects
  vector[N_4] r_4_bias_5;  // actual group-level effects
  vector[N_4] r_4_bias_6;  // actual group-level effects
  vector[N_4] r_4_bias_7;  // actual group-level effects
  vector[N_4] r_4_bias_8;  // actual group-level effects
  vector[N_4] r_4_bias_9;  // actual group-level effects
  vector[N_4] r_4_bias_10;  // actual group-level effects
  vector[N_4] r_4_bias_11;  // actual group-level effects
  vector[N_4] r_4_bias_12;  // actual group-level effects
  real lprior = 0;  // prior contributions to the log posterior
  r_1_1 = (sd_1[1] * (z_1[1]));
  r_1_2 = (sd_1[2] * (z_1[2]));
  r_1_3 = (sd_1[3] * (z_1[3]));
  r_1_4 = (sd_1[4] * (z_1[4]));
  r_1_5 = (sd_1[5] * (z_1[5]));
  r_1_6 = (sd_1[6] * (z_1[6]));
  r_1_7 = (sd_1[7] * (z_1[7]));
  r_1_8 = (sd_1[8] * (z_1[8]));
  r_1_9 = (sd_1[9] * (z_1[9]));
  r_1_10 = (sd_1[10] * (z_1[10]));
  r_1_11 = (sd_1[11] * (z_1[11]));
  r_1_12 = (sd_1[12] * (z_1[12]));
  r_1_13 = (sd_1[13] * (z_1[13]));
  r_1_14 = (sd_1[14] * (z_1[14]));
  r_1_15 = (sd_1[15] * (z_1[15]));
  r_1_16 = (sd_1[16] * (z_1[16]));
  r_1_17 = (sd_1[17] * (z_1[17]));
  r_1_18 = (sd_1[18] * (z_1[18]));
  r_1_19 = (sd_1[19] * (z_1[19]));
  r_1_20 = (sd_1[20] * (z_1[20]));
  r_1_21 = (sd_1[21] * (z_1[21]));
  r_1_22 = (sd_1[22] * (z_1[22]));
  r_1_23 = (sd_1[23] * (z_1[23]));
  r_1_24 = (sd_1[24] * (z_1[24]));
  r_2_bs_1 = (sd_2[1] * (z_2[1]));
  r_2_bs_2 = (sd_2[2] * (z_2[2]));
  r_2_bs_3 = (sd_2[3] * (z_2[3]));
  r_2_bs_4 = (sd_2[4] * (z_2[4]));
  r_2_bs_5 = (sd_2[5] * (z_2[5]));
  r_2_bs_6 = (sd_2[6] * (z_2[6]));
  r_2_bs_7 = (sd_2[7] * (z_2[7]));
  r_2_bs_8 = (sd_2[8] * (z_2[8]));
  r_2_bs_9 = (sd_2[9] * (z_2[9]));
  r_2_bs_10 = (sd_2[10] * (z_2[10]));
  r_2_bs_11 = (sd_2[11] * (z_2[11]));
  r_2_bs_12 = (sd_2[12] * (z_2[12]));
  r_3_ndt_1 = (sd_3[1] * (z_3[1]));
  r_3_ndt_2 = (sd_3[2] * (z_3[2]));
  r_3_ndt_3 = (sd_3[3] * (z_3[3]));
  r_3_ndt_4 = (sd_3[4] * (z_3[4]));
  r_3_ndt_5 = (sd_3[5] * (z_3[5]));
  r_3_ndt_6 = (sd_3[6] * (z_3[6]));
  r_3_ndt_7 = (sd_3[7] * (z_3[7]));
  r_3_ndt_8 = (sd_3[8] * (z_3[8]));
  r_3_ndt_9 = (sd_3[9] * (z_3[9]));
  r_3_ndt_10 = (sd_3[10] * (z_3[10]));
  r_3_ndt_11 = (sd_3[11] * (z_3[11]));
  r_3_ndt_12 = (sd_3[12] * (z_3[12]));
  r_4_bias_1 = (sd_4[1] * (z_4[1]));
  r_4_bias_2 = (sd_4[2] * (z_4[2]));
  r_4_bias_3 = (sd_4[3] * (z_4[3]));
  r_4_bias_4 = (sd_4[4] * (z_4[4]));
  r_4_bias_5 = (sd_4[5] * (z_4[5]));
  r_4_bias_6 = (sd_4[6] * (z_4[6]));
  r_4_bias_7 = (sd_4[7] * (z_4[7]));
  r_4_bias_8 = (sd_4[8] * (z_4[8]));
  r_4_bias_9 = (sd_4[9] * (z_4[9]));
  r_4_bias_10 = (sd_4[10] * (z_4[10]));
  r_4_bias_11 = (sd_4[11] * (z_4[11]));
  r_4_bias_12 = (sd_4[12] * (z_4[12]));
  lprior += normal_lpdf(b | 0, 5);
  lprior += normal_lpdf(b_bs | 2.5, 1)
    - 12 * normal_lccdf(0 | 2.5, 1);
  lprior += normal_lpdf(b_ndt | 0.1, 0.1)
    - 12 * log_diff_exp(normal_lcdf(0.15 | 0.1, 0.1), normal_lcdf(0 | 0.1, 0.1));
  lprior += normal_lpdf(b_bias | 0.5, 0.25)
    - 12 * log_diff_exp(normal_lcdf(1 | 0.5, 0.25), normal_lcdf(0 | 0.5, 0.25));
  lprior += normal_lpdf(sd_1 | 0, 0.3)
    - 24 * normal_lccdf(0 | 0, 0.3);
  lprior += student_t_lpdf(sd_2 | 3, 0, 2.5)
    - 12 * student_t_lccdf(0 | 3, 0, 2.5);
  lprior += student_t_lpdf(sd_3 | 3, 0, 2.5)
    - 12 * student_t_lccdf(0 | 3, 0, 2.5);
  lprior += student_t_lpdf(sd_4 | 3, 0, 2.5)
    - 12 * student_t_lccdf(0 | 3, 0, 2.5);
}
model {
  // likelihood including constants
  if (!prior_only) {
    // initialize linear predictor term
    vector[N] mu = rep_vector(0.0, N);
    // initialize linear predictor term
    vector[N] bs = rep_vector(0.0, N);
    // initialize linear predictor term
    vector[N] ndt = rep_vector(0.0, N);
    // initialize linear predictor term
    vector[N] bias = rep_vector(0.0, N);
    mu += X * b;
    bs += X_bs * b_bs;
    ndt += X_ndt * b_ndt;
    bias += X_bias * b_bias;
    for (n in 1:N) {
      // add more terms to the linear predictor
      mu[n] += r_1_1[J_1[n]] * Z_1_1[n] + r_1_2[J_1[n]] * Z_1_2[n] + r_1_3[J_1[n]] * Z_1_3[n] + r_1_4[J_1[n]] * Z_1_4[n] + r_1_5[J_1[n]] * Z_1_5[n] + r_1_6[J_1[n]] * Z_1_6[n] + r_1_7[J_1[n]] * Z_1_7[n] + r_1_8[J_1[n]] * Z_1_8[n] + r_1_9[J_1[n]] * Z_1_9[n] + r_1_10[J_1[n]] * Z_1_10[n] + r_1_11[J_1[n]] * Z_1_11[n] + r_1_12[J_1[n]] * Z_1_12[n] + r_1_13[J_1[n]] * Z_1_13[n] + r_1_14[J_1[n]] * Z_1_14[n] + r_1_15[J_1[n]] * Z_1_15[n] + r_1_16[J_1[n]] * Z_1_16[n] + r_1_17[J_1[n]] * Z_1_17[n] + r_1_18[J_1[n]] * Z_1_18[n] + r_1_19[J_1[n]] * Z_1_19[n] + r_1_20[J_1[n]] * Z_1_20[n] + r_1_21[J_1[n]] * Z_1_21[n] + r_1_22[J_1[n]] * Z_1_22[n] + r_1_23[J_1[n]] * Z_1_23[n] + r_1_24[J_1[n]] * Z_1_24[n];
    }
    for (n in 1:N) {
      // add more terms to the linear predictor
      bs[n] += r_2_bs_1[J_2[n]] * Z_2_bs_1[n] + r_2_bs_2[J_2[n]] * Z_2_bs_2[n] + r_2_bs_3[J_2[n]] * Z_2_bs_3[n] + r_2_bs_4[J_2[n]] * Z_2_bs_4[n] + r_2_bs_5[J_2[n]] * Z_2_bs_5[n] + r_2_bs_6[J_2[n]] * Z_2_bs_6[n] + r_2_bs_7[J_2[n]] * Z_2_bs_7[n] + r_2_bs_8[J_2[n]] * Z_2_bs_8[n] + r_2_bs_9[J_2[n]] * Z_2_bs_9[n] + r_2_bs_10[J_2[n]] * Z_2_bs_10[n] + r_2_bs_11[J_2[n]] * Z_2_bs_11[n] + r_2_bs_12[J_2[n]] * Z_2_bs_12[n];
    }
    for (n in 1:N) {
      // add more terms to the linear predictor
      ndt[n] += r_3_ndt_1[J_3[n]] * Z_3_ndt_1[n] + r_3_ndt_2[J_3[n]] * Z_3_ndt_2[n] + r_3_ndt_3[J_3[n]] * Z_3_ndt_3[n] + r_3_ndt_4[J_3[n]] * Z_3_ndt_4[n] + r_3_ndt_5[J_3[n]] * Z_3_ndt_5[n] + r_3_ndt_6[J_3[n]] * Z_3_ndt_6[n] + r_3_ndt_7[J_3[n]] * Z_3_ndt_7[n] + r_3_ndt_8[J_3[n]] * Z_3_ndt_8[n] + r_3_ndt_9[J_3[n]] * Z_3_ndt_9[n] + r_3_ndt_10[J_3[n]] * Z_3_ndt_10[n] + r_3_ndt_11[J_3[n]] * Z_3_ndt_11[n] + r_3_ndt_12[J_3[n]] * Z_3_ndt_12[n];
    }
    for (n in 1:N) {
      // add more terms to the linear predictor
      bias[n] += r_4_bias_1[J_4[n]] * Z_4_bias_1[n] + r_4_bias_2[J_4[n]] * Z_4_bias_2[n] + r_4_bias_3[J_4[n]] * Z_4_bias_3[n] + r_4_bias_4[J_4[n]] * Z_4_bias_4[n] + r_4_bias_5[J_4[n]] * Z_4_bias_5[n] + r_4_bias_6[J_4[n]] * Z_4_bias_6[n] + r_4_bias_7[J_4[n]] * Z_4_bias_7[n] + r_4_bias_8[J_4[n]] * Z_4_bias_8[n] + r_4_bias_9[J_4[n]] * Z_4_bias_9[n] + r_4_bias_10[J_4[n]] * Z_4_bias_10[n] + r_4_bias_11[J_4[n]] * Z_4_bias_11[n] + r_4_bias_12[J_4[n]] * Z_4_bias_12[n];
    }
    for (n in 1:N) {
      target += wiener_diffusion_lpdf(Y[n] | dec[n], bs[n], ndt[n], bias[n], mu[n]);
    }
  }
  // priors including constants
  target += lprior;
  target += std_normal_lpdf(z_1[1]);
  target += std_normal_lpdf(z_1[2]);
  target += std_normal_lpdf(z_1[3]);
  target += std_normal_lpdf(z_1[4]);
  target += std_normal_lpdf(z_1[5]);
  target += std_normal_lpdf(z_1[6]);
  target += std_normal_lpdf(z_1[7]);
  target += std_normal_lpdf(z_1[8]);
  target += std_normal_lpdf(z_1[9]);
  target += std_normal_lpdf(z_1[10]);
  target += std_normal_lpdf(z_1[11]);
  target += std_normal_lpdf(z_1[12]);
  target += std_normal_lpdf(z_1[13]);
  target += std_normal_lpdf(z_1[14]);
  target += std_normal_lpdf(z_1[15]);
  target += std_normal_lpdf(z_1[16]);
  target += std_normal_lpdf(z_1[17]);
  target += std_normal_lpdf(z_1[18]);
  target += std_normal_lpdf(z_1[19]);
  target += std_normal_lpdf(z_1[20]);
  target += std_normal_lpdf(z_1[21]);
  target += std_normal_lpdf(z_1[22]);
  target += std_normal_lpdf(z_1[23]);
  target += std_normal_lpdf(z_1[24]);
  target += std_normal_lpdf(z_2[1]);
  target += std_normal_lpdf(z_2[2]);
  target += std_normal_lpdf(z_2[3]);
  target += std_normal_lpdf(z_2[4]);
  target += std_normal_lpdf(z_2[5]);
  target += std_normal_lpdf(z_2[6]);
  target += std_normal_lpdf(z_2[7]);
  target += std_normal_lpdf(z_2[8]);
  target += std_normal_lpdf(z_2[9]);
  target += std_normal_lpdf(z_2[10]);
  target += std_normal_lpdf(z_2[11]);
  target += std_normal_lpdf(z_2[12]);
  target += std_normal_lpdf(z_3[1]);
  target += std_normal_lpdf(z_3[2]);
  target += std_normal_lpdf(z_3[3]);
  target += std_normal_lpdf(z_3[4]);
  target += std_normal_lpdf(z_3[5]);
  target += std_normal_lpdf(z_3[6]);
  target += std_normal_lpdf(z_3[7]);
  target += std_normal_lpdf(z_3[8]);
  target += std_normal_lpdf(z_3[9]);
  target += std_normal_lpdf(z_3[10]);
  target += std_normal_lpdf(z_3[11]);
  target += std_normal_lpdf(z_3[12]);
  target += std_normal_lpdf(z_4[1]);
  target += std_normal_lpdf(z_4[2]);
  target += std_normal_lpdf(z_4[3]);
  target += std_normal_lpdf(z_4[4]);
  target += std_normal_lpdf(z_4[5]);
  target += std_normal_lpdf(z_4[6]);
  target += std_normal_lpdf(z_4[7]);
  target += std_normal_lpdf(z_4[8]);
  target += std_normal_lpdf(z_4[9]);
  target += std_normal_lpdf(z_4[10]);
  target += std_normal_lpdf(z_4[11]);
  target += std_normal_lpdf(z_4[12]);
}
generated quantities {
}