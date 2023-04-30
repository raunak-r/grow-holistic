package com.example.demo.tables;

import jakarta.persistence.*;
import lombok.Data;
import org.hibernate.engine.internal.Cascade;

import java.util.ArrayList;
import java.util.List;

@Data
@Entity
@Table(name="Users")
public class users {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;
    private String name;
    private String email;

    @OneToMany(cascade=CascadeType.ALL,fetch = FetchType.LAZY)
    private List<orders> orders=new ArrayList<>();
}
