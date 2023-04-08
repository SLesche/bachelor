# This file should install all the necessary packages and maybe check if 
# all datafiles required are there

maybe_install <- function(pkgs, type = "both"){
  for (pkg in pkgs){
    if (!pkg %in% rownames(installed.packages())){
      install.packages(pkg, type = type)
    }
  }

}
ensure_setup <- function(){
  if (R.Version()$major != "4" | R.Version()$minor != "1.3"){
    stop("Please use R 4.1.3!")
  }
  
  maybe_install("devtools")
  
  if (!devtools::find_rtools()){
    stop("You need to have rtools40 installed")
  }
  
  maybe_install(c("rstudioapi", "renv", "MASS"))
  
  if (rstudioapi::getActiveProject() == ""){
    stop("Please open the .Rproj file in the bachelor-main folder")
  }
  
  maybe_install(c("brms", "shinystan", "threejs", "igraph"), type = "binary")
  
  if (list.files("./", pattern = ".lock") != "renv.lock"){
    stop("Ensure you have lockfile!")
  }
  
  if (!dir.exists("./markdown/output")){
    dir.create("./markdown/output")
    print("Created output subfolder")
  }
  
  if (!dir.exists("./markdown/data")){
    dir.create("./markdown/data")
    print("Created data subfolder")
  }
  
  print("Checking renv-lockfile")
  print("Updating packages required")
  renv::restore(exclude = c("cmdstanr", "brms", "threejs", "MASS", "igraph"))
  print("All packages installed")
}

render_project <- function(output = "pdf"){
  n_output = length(output)
  # Check for pdf in output because of tinytex
  if("pdf" %in% output){
    if("tinytex" %in% rownames(installed.packages())){
      install.packages("tinytex")
    }
    if(tinytex::is_tinytex() || Sys.which("miktex_console.exe") != ""){
      print("No proper TeX engine found. Installing tinytex.")
      tinytex::install_tinytex()
    }
  }
  
  # Check for cache folders
  if(!dir.exists("./markdown/master_cache")){
    print("No computations cached yet. Regenerating full project. This may take some time.")
  }
  for (i in 1:n_output){
    if (output[i] != "pdf" & output[i] != "word"){
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
