# Sven Lesche's Bachelor Thesis
This repository contains all scripts used to generate the bachelor thesis: _"Effects of the Response-Stimulus-Interval on the Nature of Cognitive Processes Underlying Post-Error Slowing – A Diffusion Model Account"_.
To replicate my work, please inquire about the raw data used, I'll gladly provide it. 

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
