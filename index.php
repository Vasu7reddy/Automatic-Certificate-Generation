<?php

$last_line = system('python index.py winner --name=dharshan --degree=BCA --place=First --competition="comp" --year=2021', $return_val);
echo $return_val;