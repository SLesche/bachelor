# This file knits the master.rmd document
for (i in c("papaja::apa6_pdf", "papaja::apa6_word")){
  rmarkdown::render(
    input = "./markdown/master.rmd",
    output_format = i,
    output_dir = "markdown/output",
    output_file = paste0("bachelor_thesis_sl"),
    intermediates_dir = "markdown",
    knit_root_dir = file.path(rprojroot::find_rstudio_root_file()),
    clean = TRUE
    # params = params # can set author and date in a vector here
  )
}

rmarkdown::render(
  input = "./markdown/master.rmd",
  output_format = "papaja::apa6_pdf",
  output_dir = "markdown/output",
  output_file = paste0("bachelor_thesis_sl"),
  intermediates_dir = "markdown",
  knit_root_dir = file.path(rprojroot::find_rstudio_root_file()),
  clean = TRUE
  # params = params # can set author and date in a vector here
)
