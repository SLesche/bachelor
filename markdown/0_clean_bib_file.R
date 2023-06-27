bib_file <- read_file(file = "./markdown/pes_lib.bib")

no_type <- stringr::str_replace_all(bib_file, "type = \\{.+\\}", "") 

write_file(no_type, file = "./markdown/clean_pes_lib.bib")
