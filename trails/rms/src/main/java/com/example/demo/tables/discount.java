package com.example.demo.tables;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name="discount")
public class discount {
    @Id
    private int dis_id;
    private int dis_price;

    @OneToOne
    @JoinColumn(name = "order_id",nullable = false)
    private orders order;

}
