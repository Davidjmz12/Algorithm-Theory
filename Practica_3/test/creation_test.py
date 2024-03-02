def create_test_file_1(width,height,scale,test_name):
    with open(test_name,"w") as f:
        f.write(f"{width*height} {height*scale} {width*scale}\n")
        for i in range(0,width):
            for j in range(0,height):
                f.write(f"{scale} {scale} {scale*j} {scale*i}\n")
                
        f.write(f"{width} {width*scale} {width*scale}\n")
        for i in range(1,width+1):
           f.write(f"{scale*i} {scale*i} 0 0\n")
        
        f.write(f"{height-1} {height*scale} {height*scale}\n")
        for i in range(0,height-1):
            f.write(f"{scale*2} {scale*2} {scale*i} {scale*i}\n")
        
        f.write(f"{width*2} {width*scale} {width*scale}\n")
        for i in range(0,width):
            f.write(f"{scale} {(width-i)*scale} {scale*i} {scale*i}\n{scale*(width-i)} {scale} {scale*i} {scale*i}\n")
        
                
create_test_file_1(10,10,10,"test/in/test2.txt")