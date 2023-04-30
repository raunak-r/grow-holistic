package com.example.demo.tables;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name="Users")
public class users {
    @Id

    private int id;
    private String name;
    private String email;
}
