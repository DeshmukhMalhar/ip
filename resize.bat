@echo on
mkdir res
set "source_folder=g:\ip\untitled"
set "result_folder_1=g:\ip\untitled\res"

for %%a in ("%source_folder%\*jpg") do (
   call resize.bat -source "%%~fa" -target "%result_folder_1%\%%~nxa" -max-height 480 -max-width 640 -keep-ratio no -force yes
)
