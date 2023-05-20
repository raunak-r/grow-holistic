package com.example.demo.tables;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;

@Data
@Entity
@Table(name="Restaurants")
public class res {
    @Id
    private int res_id;
    private String res_name;
    private String city;

    @OneToMany(mappedBy = "res")
    private List<items> items = new ArrayList<>();

}



