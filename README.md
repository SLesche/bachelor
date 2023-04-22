# Sven Lesche's Bachelor Thesis
This repository contains all scripts used to generate the bachelor thesis: _"The Nature of Cognitive Processes Underlying Post-Error Slowing – A Diffusion Model Account"_.

# Replicating this work
R-Version 4.1.3 is required to replicate this work. You can install it [here](https://cran.r-project.org/bin/windows/base/old/4.1.3/). [rtools40](https://cran.r-project.org/bin/windows/Rtools/rtools40.html) is also required to compile some of the packages used.

After installing R 4.1.3 and rtools40, open RStudio and open the file `ba_written.Rproj` to open up a new project in RStudio. Then head over to the script `markdown/0_create_report.R`. The script first sources helper functions that will be used to ensure correct package installation and project setup. `render_project()` runs these functions, installs all necessary packages, installs [tinytex](https://yihui.org/tinytex/) if needed and knits the project. This will take the raw data, compute everything except fitting the DDM used in this work and render the final report.

# Dependencies and folder structure

## Renv
To ensure the longevity of this work, the package `renv` was used to generate a project-specific library containing certain versions of the other packages used. You might need to install the `renv` package and call `renv::activate()` after cloning this repository. Check `renv::status()`to compare your current package versions to those used by me. `renv::restore()` will update/revert all packages in the project-specific library to the versions used in my original analysis. This will not affect the packages installed in your global library! As soon as you switch to another project, R will use your package-versions again.
For more information on `renv`, consult [this introduction](https://rstudio.github.io/renv/articles/renv.html).

## Markdown
This subfolder contains files used to generate the text itself, aswell as all analysis conducted prior to and following the experiment.
Report-generation depends heavily on the `papaja` package and its apa6-template. Some changes were done to ensure APA7-compatability. See [this guide](https://www.martinasladek.co.uk/post/how-to-set-up-papaja-to-work-with-apa-7-format/) to find out how.

## Psychopy
This subfolder contains files responsible for generating the task in PsychoPy. Instructions slides can be sent on request.

## Python
This subfolder contains files pertaining to all analysis done in Python. It's useless for now, but might contain HDDM-analysis at some point in time
