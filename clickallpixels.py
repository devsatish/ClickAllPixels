#!/usr/bin/python

import objc


class ETMouse():    
    def setMousePosition(self, x, y):
        bndl = objc.loadBundle('CoreGraphics', globals(), 
                '/System/Library/Frameworks/ApplicationServices.framework')
        objc.loadBundleFunctions(bndl, globals(), 
                [('CGWarpMouseCursorPosition', 'v{CGPoint=ff}')])
        CGWarpMouseCursorPosition((x, y))

if __name__ == "__main__":
    et = ETMouse()
    x = (20,30, 719)
    y =  (114, 300, 663)
    for i, j in zip(x, y):
    	et.setMousePosition(i,j)
