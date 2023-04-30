package com.example.demo.tables;

import jakarta.persistence.*;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;

@Data
@Entity
@Table(name = "items")
public class items {
    @Id
    private int item_id;
    private String item_name;
    private float price;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "res_id", nullable = false)
    private res res;
    @OneToOne(cascade = CascadeType.ALL)
    private orders order;
}
