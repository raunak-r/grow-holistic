package com.sbs.firstDemoSB;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class firstClass
{
    @GetMapping("/welcome")
    public String welcome(){
        System.out.println("this is a print statement");
        return "this is first class";
    }
}
