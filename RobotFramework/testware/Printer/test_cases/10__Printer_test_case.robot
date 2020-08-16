*** Settings ***
Documentation    Review of the different modules of the K300G printer.

Library       ../libraries/Printer_wrapper.py
Library       ../../commons/robot_framework_utilities.py
Force Tags    printer-tests

*** Test Cases ***
Validate printer version
    [Documentation]    Compare the model and version 
    ...                of the current printer be K300G V0.28
    [Tags]    printer-version  command
    ${printer_version}=  get printer version
    Should Be Equal As Strings  ${printer_version}  K300G V0.28

Validate printer temperature
    [Documentation]    Verify that the printer temperature 
    ...                does not exceed 30 degrees Celcius
    [Tags]    printer-temperature  command
    ${printer_temperture}=  get printer temperature
    ${result}=  should be less than  ${printer_temperture}  30
    Should Be True  ${result}

Validate printer volt
    [Documentation]    Validate that the printer voltage 
    ...                is 16V when it is connected to the power cable
    [Tags]    printer-volt  command
    ${printer_volt}=  get printer volt
    should be Equal  ${printer_volt}  16V 

Validate status printer connected with paper
    [Documentation]    'Printer connected with paper',
    ...                'MIR conectado', 'Fim da Impressão', 
    ...                'MIR com papel', 'MIR sem atolamento',
    ...                'MIR sem problemas' 
    [Tags]   printer-connected-with-paper  command
    FOR    ${waiting_for_tester}    IN RANGE    1    60
           ${printer_status}=  get printer status
           Exit For Loop IF    ${printer_status} == 32
           sleep  1s
    END
    should Be Equal As Integers  ${printer_status}  32

Validate status printer connected without paper
    [Documentation]    'Printer connected without paper',
    ...                'MIR conectado', 'Fim da Impressão',
    ...                'MIR sem papel', 'MIR sem atolamento',
    ...                'MIR con problemas
    [Tags]    Printer-connected-without-paper  command
    FOR    ${waiting_for_tester}    IN RANGE    1    60
           ${printer_status}=  get printer status
           Exit For Loop IF    ${printer_status} == 20
           sleep  1s
    END
    should Be Equal As Integers  ${printer_status}  20

Validate status paper Jam
    [Documentation]    'Paper Jam', 'MIR conectado',
    ...                'Fim da Impressão', 'MIR com papel',
    ...                'MIR con atolamento', 'MIR con problemas'
    [Tags]    paper-Jam  command
    FOR    ${waiting_for_tester}    IN RANGE    1    60
           ${printer_status}=  get printer status 
           Exit For Loop IF    ${printer_status} == 84
           sleep  1s
    END
    should Be Equal As Integers  ${printer_status}  84 

validate file printing
    [Documentation]    Validate that file printing works correctly
    [Tags]    print-file  job 
    Log To Console  ¿Ready to Print?: True or False
    print file  /data/printerfiles/Imagem_Anexo_II_Item_201.png 
    Log To Console  ¿printed correctly?: True or False
    ${result_test} =  insert test comment
    should be true  ${result_test} 


