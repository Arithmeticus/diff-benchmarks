<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   xmlns:tan="tag:textalign.net,2015:ns"
   xmlns:xs="http://www.w3.org/2001/XMLSchema"
   xmlns:math="http://www.w3.org/2005/xpath-functions/math"
   version="3.0">
   <xsl:include href="../../../TAN/TAN-2022/functions-2/TAN-function-library.xsl"/>
   
   <!-- Catalyzing input: any XML file including this one -->
   <!-- Secondary input: parameters, below -->
   <!-- Main output: diagnostics -->
   <!-- Secondary output: none -->
   
   <xsl:output indent="yes"/>
   <xsl:param name="tan:validation-mode-on" as="xs:boolean" select="false()"/>
   <xsl:param name="controlled-length" as="xs:string" select="'100'"/>
   <xsl:param name="corrupt-n" as="xs:string?" select="'1'"/>
   
   <xsl:variable name="target-a-uri"
      select="resolve-uri('speedtest' || $controlled-length || '/cfr' || $controlled-length || '-corrupt-0.txt', static-base-uri())"
   />
   <xsl:variable name="target-b-uri"
      select="resolve-uri('speedtest' || $controlled-length || '/cfr' || $controlled-length || '-corrupt-' || $corrupt-n || '.txt', static-base-uri())"
   />
   
   <xsl:variable name="string-a" as="xs:string?" select="unparsed-text($target-a-uri)"/>
   <xsl:variable name="string-b" as="xs:string?" select="unparsed-text($target-b-uri)"/>
   
   
   <xsl:template match="/">
      <xsl:message select="'attenuation rate ' || string($tan:diff-sample-size-attenuation-rate)"/>
      <xsl:message select="'attenuation base ' || string($tan:diff-sample-size-attenuation-base)"/>
      <xsl:message select="'horiz pass frequency ' || string($tan:diff-horizontal-pass-frequency-rate)"/>
      <xsl:message select="'max sample ' || string($tan:diff-maximum-number-of-horizontal-passes)"/>
      <xsl:copy-of select="tan:diff($string-a, $string-b, false())"/>
   </xsl:template>
   
</xsl:stylesheet>