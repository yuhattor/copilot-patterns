#!/bin/sh
 
echo '<html><body>'
sed 's/^.*/<a href="&">&<\/a><br\/>/'
echo '</body></html>'