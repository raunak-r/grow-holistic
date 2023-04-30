package com.example.demo.tables;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name = "items")
public class items {
    @Id
    private int item_id;
    private String item_name;
    private float price;

    private int res_id;
}
