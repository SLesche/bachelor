add_prefix_chunk_labels <- function(file){
  if (file.exists(file)){
    # Extract file name
    file_name_extenstion <- stringr::str_extract(
      file,
      "([^/]+)(?:\\.[*]+)?$"
    )
    
    file_name <- stringr::str_extract(
      file_name_extenstion,
      "([^\\.]+)"
    )
    # Read in the File
    lines <- readLines(file)
    
    # Remove potential duplicate labels already exsiting
    no_prefix <- stringr::str_replace_all(
      lines, 
      paste0(
        "r ",
        stringr::str_replace_all(file_name, "_", "-"),
        "-"
      ), 
      "r "
    )
    # Change code labels
    replaced_lables <- stringr::str_replace(
      no_prefix,
      "(```\\{r[ ]+)([^,}]+)",
      paste0(
        "\\1",
        stringr::str_replace_all(file_name, "_", "-"),
        "-",
        "\\2")
    )
    # Deal with "child" labels
    # write to new file
    readr::write_lines(replaced_lables, file = file)
  } 
  else {
    print(file)
    stop("This file doesn't exist")
  }
}

rmd_files <- list.files("./markdown/", pattern = ".Rmd")

files_to_alter <- paste0("./markdown/", rmd_files[-which(rmd_files == "master.Rmd")])

for (i in files_to_alter){
  add_prefix_chunk_labels(i)
}

