# Parsing list Directory Number from  Cisco unified Communications Manager

In folder shema/ files AXLAPI.wsdl, AXLEnums.xsd and AXLSoap.xsd. Unzip this file from axlsqltoolkit.zip in Plugins CUCM (Application->Plugins)

Output format file cucm_dn.txt:
```txt
(reply){
   return = 
      (return){
         line[] = 
            (LLine){
               _uuid = "{}"
               pattern = "1733039"
               description = "Reception"
               usage = "Device"
               shareLineAppearanceCssName = 
                  (shareLineAppearanceCssName){
                     value = "lpu_limited_css"
                     _uuid = "{}"
                  }
                  .
                  .
                  .
           },
      }
 }
```
Output format file css.txt:
```
{'number': '"1707444"', 'description': ['"Test"'], 'css': '"ast_limited_css"'}
{'number': '"1707278"', 'description': ['"FAX"'], 'css': '"ast_limited_css"'}
.
{'number': '"1707278"', 'description': ['"FAX"'], 'css': '"ast_limited_css"'}
```
