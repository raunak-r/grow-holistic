package com.example.demo.tables;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name="menu")
public class menu {
    @Id
    private int menu_id;
    private String dish_name;
}