# This file should install all the necessary packages and maybe check if 
# all datafiles required are there
ensure_setup <- function(){
  if (R.Version()$major != "4" | R.Version()$minor != "1.3"){
    stop("Please use R 4.1.3!")
  }
  
  if (!"renv" %in% rownames(installed.packages())){
    install.packages("renv")
  }
  
  if (list.files("./", pattern = ".lock") != "renv.lock"){
    stop("Ensure you have lockfile!")
  }
  
  if (!dir.exists("./markdown/output")){
    dir.create("./markdown/output")
    print("Created output subfolder")
  }
  
  print("Checking renv-lockfile")
  print("Updating packages required")
  renv::restore(exclude = c("cmdstanr"))
  print("All packages installed")
}

render_project <- function(output = "pdf"){
  n_output = length(output)
  for (i in 1:n_output){
    if (output[i] != "pdf" | output[i] != "word"){
      stop("Only word and pdf are valid output types")
    }
    output_format = paste0("papaja::apa6_", output[i])
    
    rmarkdown::render(
      input = "./markdown/master.rmd",
      output_format = output_format,
      output_dir = "markdown/output",
      output_file = paste0("bachelor_thesis_sl"),
      intermediates_dir = "markdown",
      knit_root_dir = file.path(rprojroot::find_rstudio_root_file()),
      clean = TRUE
      # params = params # can set author and date in a vector here
    )
  }
}
