ROYAL_MAIL_RATING_REQUEST = {
    "method": "GET",
    "url": "https://api.clickanddrop.royalmail.com/olp-partner/v4/shippingServices",
    "parameters": {
        "country": {
            "value": "GBR",
            "in": "query"
        },
        "weight": {
            "value": "1000",
            "in": "query"
        }
    },
    "headers": {
        "X-Partner-Token": "0000-0000-0000-0000"
    }
}

ROYAL_MAIL_SUCCESSFUL_RATING_RESPONSE = {
    "status_code": 200,
    "headers": {
        "Transfer-Encoding": "chunked",
        "Content-Type": "application/json; charset=utf-8",
        "Content-Encoding": "gzip",
        "Vary": "Accept-Encoding",
        "AccessToken": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "api-supported-versions": "2.0,3.0,4.0",
        "api-deprecated-versions": "1.0",
        "X-Correlation-Id": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Referrer-Policy": "no-referrer",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "SAMEORIGIN",
        "X-XSS-Protection": "1; mode=block",
        "Date": "Fri, 04 Jul 2025 17:04:44 GMT"
    },
    "body": {
        "shippingServices": [
            {
                "brandType": "RoyalMail",
                "shippingServiceIdentifier": "TOLP24",
                "shippingServiceDisplayName": "Tracked 24",
                "countryIso3Code": "GBR",
                "minWeightInGrams": 751,
                "maxWeightInGrams": 1000,
                "isEligibleForCollection": True,
                "isEligibleForCollectionSafePlace": True,
                "isEligibleForDeliverySafePlace": True,
                "isEligibleForLabellessCollections": True,
                "isEligibleForLabelsToGo": True,
                "packageFormats": [
                    {
                        "packageFormatIdentifier": "MediumParcel",
                        "packageFormatDisplayName": "Medium Parcel",
                        "maxDimensions": {
                            "widthInMm": 460,
                            "heightInMm": 610,
                            "depthInMm": 460
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 4.79,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "SmallParcel",
                        "packageFormatDisplayName": "Small Parcel",
                        "maxDimensions": {
                            "widthInMm": 350,
                            "heightInMm": 450,
                            "depthInMm": 160
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 3.4,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "LargeLetter",
                        "packageFormatDisplayName": "Large Letter",
                        "maxDimensions": {
                            "widthInMm": 250,
                            "heightInMm": 353,
                            "depthInMm": 25
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 2.8,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": []
                            },
                            "parcelshop": {
                                "supplementCharges": []
                            }
                        }
                    }
                ],
                "enhancements": [
                    "Tracked",
                    "EmailAndSmsNotification"
                ],
                "serviceLevel": "_24",
                "dropOffLocations": {
                    "postBox": True,
                    "parcelBox": True,
                    "postOffice": True,
                    "deliveryOffice": True,
                    "parcelshop": True
                },
                "standardCollectionPrice": 0.0
            },
            {
                "brandType": "RoyalMail",
                "shippingServiceIdentifier": "TOLP24SFA",
                "shippingServiceDisplayName": "Tracked 24 with Age Verification",
                "countryIso3Code": "GBR",
                "minWeightInGrams": 751,
                "maxWeightInGrams": 1000,
                "isEligibleForCollection": True,
                "isEligibleForCollectionSafePlace": True,
                "isEligibleForDeliverySafePlace": False,
                "isEligibleForLabellessCollections": True,
                "isEligibleForLabelsToGo": False,
                "packageFormats": [
                    {
                        "packageFormatIdentifier": "MediumParcel",
                        "packageFormatDisplayName": "Medium Parcel",
                        "maxDimensions": {
                            "widthInMm": 460,
                            "heightInMm": 610,
                            "depthInMm": 460
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 7.1,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": False
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "SmallParcel",
                        "packageFormatDisplayName": "Small Parcel",
                        "maxDimensions": {
                            "widthInMm": 350,
                            "heightInMm": 450,
                            "depthInMm": 160
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 5.7,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": False
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    }
                ],
                "enhancements": [
                    "Tracked",
                    "Signed",
                    "AgeVerification",
                    "EmailAndSmsNotification"
                ],
                "serviceLevel": "_24",
                "dropOffLocations": {
                    "postBox": True,
                    "parcelBox": True,
                    "postOffice": True,
                    "deliveryOffice": True,
                    "parcelshop": True
                },
                "standardCollectionPrice": 0.0
            },
            {
                "brandType": "RoyalMail",
                "shippingServiceIdentifier": "TOLP24SF",
                "shippingServiceDisplayName": "Tracked 24 with Signature",
                "countryIso3Code": "GBR",
                "minWeightInGrams": 751,
                "maxWeightInGrams": 1000,
                "isEligibleForCollection": True,
                "isEligibleForCollectionSafePlace": True,
                "isEligibleForDeliverySafePlace": False,
                "isEligibleForLabellessCollections": True,
                "isEligibleForLabelsToGo": True,
                "packageFormats": [
                    {
                        "packageFormatIdentifier": "MediumParcel",
                        "packageFormatDisplayName": "Medium Parcel",
                        "maxDimensions": {
                            "widthInMm": 460,
                            "heightInMm": 610,
                            "depthInMm": 460
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 5.91,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "SmallParcel",
                        "packageFormatDisplayName": "Small Parcel",
                        "maxDimensions": {
                            "widthInMm": 350,
                            "heightInMm": 450,
                            "depthInMm": 160
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 4.52,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "LargeLetter",
                        "packageFormatDisplayName": "Large Letter",
                        "maxDimensions": {
                            "widthInMm": 250,
                            "heightInMm": 353,
                            "depthInMm": 25
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 4.16,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": []
                            },
                            "parcelshop": {
                                "supplementCharges": []
                            }
                        }
                    }
                ],
                "enhancements": [
                    "Tracked",
                    "Signed",
                    "EmailAndSmsNotification"
                ],
                "serviceLevel": "_24",
                "dropOffLocations": {
                    "postBox": True,
                    "parcelBox": True,
                    "postOffice": True,
                    "deliveryOffice": True,
                    "parcelshop": True
                },
                "standardCollectionPrice": 0.0
            },
            {
                "brandType": "RoyalMail",
                "shippingServiceIdentifier": "TOLP48",
                "shippingServiceDisplayName": "Tracked 48",
                "countryIso3Code": "GBR",
                "minWeightInGrams": 751,
                "maxWeightInGrams": 1000,
                "isEligibleForCollection": True,
                "isEligibleForCollectionSafePlace": True,
                "isEligibleForDeliverySafePlace": True,
                "isEligibleForLabellessCollections": True,
                "isEligibleForLabelsToGo": True,
                "packageFormats": [
                    {
                        "packageFormatIdentifier": "MediumParcel",
                        "packageFormatDisplayName": "Medium Parcel",
                        "maxDimensions": {
                            "widthInMm": 460,
                            "heightInMm": 610,
                            "depthInMm": 460
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 4.03,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "SmallParcel",
                        "packageFormatDisplayName": "Small Parcel",
                        "maxDimensions": {
                            "widthInMm": 350,
                            "heightInMm": 450,
                            "depthInMm": 160
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 2.68,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "LargeLetter",
                        "packageFormatDisplayName": "Large Letter",
                        "maxDimensions": {
                            "widthInMm": 250,
                            "heightInMm": 353,
                            "depthInMm": 25
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 2.14,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": []
                            },
                            "parcelshop": {
                                "supplementCharges": []
                            }
                        }
                    }
                ],
                "enhancements": [
                    "Tracked",
                    "EmailAndSmsNotification"
                ],
                "serviceLevel": "_48",
                "dropOffLocations": {
                    "postBox": True,
                    "parcelBox": True,
                    "postOffice": True,
                    "deliveryOffice": True,
                    "parcelshop": True
                },
                "standardCollectionPrice": 0.0
            },
            {
                "brandType": "RoyalMail",
                "shippingServiceIdentifier": "TOLP48SFA",
                "shippingServiceDisplayName": "Tracked 48 with Age Verification",
                "countryIso3Code": "GBR",
                "minWeightInGrams": 751,
                "maxWeightInGrams": 1000,
                "isEligibleForCollection": True,
                "isEligibleForCollectionSafePlace": True,
                "isEligibleForDeliverySafePlace": False,
                "isEligibleForLabellessCollections": True,
                "isEligibleForLabelsToGo": False,
                "packageFormats": [
                    {
                        "packageFormatIdentifier": "MediumParcel",
                        "packageFormatDisplayName": "Medium Parcel",
                        "maxDimensions": {
                            "widthInMm": 460,
                            "heightInMm": 610,
                            "depthInMm": 460
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 6.29,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": False
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "SmallParcel",
                        "packageFormatDisplayName": "Small Parcel",
                        "maxDimensions": {
                            "widthInMm": 350,
                            "heightInMm": 450,
                            "depthInMm": 160
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 4.96,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": False
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    }
                ],
                "enhancements": [
                    "Tracked",
                    "Signed",
                    "AgeVerification",
                    "EmailAndSmsNotification"
                ],
                "serviceLevel": "_48",
                "dropOffLocations": {
                    "postBox": True,
                    "parcelBox": True,
                    "postOffice": True,
                    "deliveryOffice": True,
                    "parcelshop": True
                },
                "standardCollectionPrice": 0.0
            },
            {
                "brandType": "RoyalMail",
                "shippingServiceIdentifier": "TOLP48SF",
                "shippingServiceDisplayName": "Tracked 48 with Signature",
                "countryIso3Code": "GBR",
                "minWeightInGrams": 751,
                "maxWeightInGrams": 1000,
                "isEligibleForCollection": True,
                "isEligibleForCollectionSafePlace": True,
                "isEligibleForDeliverySafePlace": False,
                "isEligibleForLabellessCollections": True,
                "isEligibleForLabelsToGo": True,
                "packageFormats": [
                    {
                        "packageFormatIdentifier": "MediumParcel",
                        "packageFormatDisplayName": "Medium Parcel",
                        "maxDimensions": {
                            "widthInMm": 460,
                            "heightInMm": 610,
                            "depthInMm": 460
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 5.13,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "SmallParcel",
                        "packageFormatDisplayName": "Small Parcel",
                        "maxDimensions": {
                            "widthInMm": 350,
                            "heightInMm": 450,
                            "depthInMm": 160
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 3.79,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            },
                            "parcelshop": {
                                "supplementCharges": [
                                    {
                                        "supplementType": "DropCharge",
                                        "cost": 0.1667,
                                        "vatCost": 0.0333
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "packageFormatIdentifier": "LargeLetter",
                        "packageFormatDisplayName": "Large Letter",
                        "maxDimensions": {
                            "widthInMm": 250,
                            "heightInMm": 353,
                            "depthInMm": 25
                        },
                        "costs": [
                            {
                                "compensationAmount": 150.0,
                                "cost": 3.48,
                                "vatCost": 0.0,
                                "dropOffLocations": {
                                    "labelsToGo": True
                                }
                            }
                        ],
                        "dropOffOptions": {
                            "postOffice": {
                                "supplementCharges": []
                            },
                            "parcelshop": {
                                "supplementCharges": []
                            }
                        }
                    }
                ],
                "enhancements": [
                    "Tracked",
                    "Signed",
                    "EmailAndSmsNotification"
                ],
                "serviceLevel": "_48",
                "dropOffLocations": {
                    "postBox": True,
                    "parcelBox": True,
                    "postOffice": True,
                    "deliveryOffice": True,
                    "parcelshop": True
                },
                "standardCollectionPrice": 0.0
            }
        ],
        "weightBands": [
            {
                "packageFormat": "LargeLetter",
                "weightBands": [
                    {
                        "maxWeightinGrams": 100,
                        "minCost": 2.14
                    },
                    {
                        "maxWeightinGrams": 250,
                        "minCost": 2.14
                    },
                    {
                        "maxWeightinGrams": 500,
                        "minCost": 2.14
                    },
                    {
                        "maxWeightinGrams": 750,
                        "minCost": 2.14
                    },
                    {
                        "maxWeightinGrams": 1000,
                        "minCost": 2.14
                    }
                ]
            },
            {
                "packageFormat": "MediumParcel",
                "weightBands": [
                    {
                        "maxWeightinGrams": 100,
                        "minCost": 4.03
                    },
                    {
                        "maxWeightinGrams": 250,
                        "minCost": 4.03
                    },
                    {
                        "maxWeightinGrams": 500,
                        "minCost": 4.03
                    },
                    {
                        "maxWeightinGrams": 750,
                        "minCost": 4.03
                    },
                    {
                        "maxWeightinGrams": 1000,
                        "minCost": 4.03
                    },
                    {
                        "maxWeightinGrams": 2000,
                        "minCost": 4.03
                    },
                    {
                        "maxWeightinGrams": 5000,
                        "minCost": 5.21
                    },
                    {
                        "maxWeightinGrams": 10000,
                        "minCost": 5.21
                    },
                    {
                        "maxWeightinGrams": 15000,
                        "minCost": 8.26
                    },
                    {
                        "maxWeightinGrams": 20000,
                        "minCost": 8.26
                    }
                ]
            },
            {
                "packageFormat": "SmallParcel",
                "weightBands": [
                    {
                        "maxWeightinGrams": 100,
                        "minCost": 2.68
                    },
                    {
                        "maxWeightinGrams": 250,
                        "minCost": 2.68
                    },
                    {
                        "maxWeightinGrams": 500,
                        "minCost": 2.68
                    },
                    {
                        "maxWeightinGrams": 750,
                        "minCost": 2.68
                    },
                    {
                        "maxWeightinGrams": 1000,
                        "minCost": 2.68
                    },
                    {
                        "maxWeightinGrams": 2000,
                        "minCost": 2.68
                    }
                ]
            }
        ]
    }
}

ROYAL_MAIL_UNAUTHORIZED_RATING_REQUEST = {
    "method": "GET",
    "url": "https://api.clickanddrop.royalmail.com/olp-partner/v4/shippingServices",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Host": "api.clickanddrop.royalmail.com",
        "X-Partner-Token": "INVALID_TOKEN"
    },
    "parameters": {
        "country": {
            "value": "GBR",
            "in": "query"
        },
        "weight": {
            "value": "1000",
            "in": "query"
        }
    }
}

ROYAL_MAIL_UNAUTHORIZED_RATING_RESPONSE = {
    "status_code": 401,
    "headers": {
        "Content-Length": "143",
        "Content-Type": "application/json",
        "WWW-Authenticate": "AzureApiManagementKey realm=\"https://api.clickanddrop.royalmail.com/olp-partner\",name=\"X-Partner-Token\",type=\"header\"",
        "Date": "Wed, 16 Jul 2025 13:57:37 GMT"
    },
    "body": {
        "statusCode": 401,
        "message": "Access denied due to invalid subscription key. Make sure to provide a valid key for an active subscription."
    }
}

ROYAL_MAIL_BAD_REQUEST_RATING_REQUEST = {
    "method": "GET",
    "url": "https://api.clickanddrop.royalmail.com/olp-partner/v4/shippingServices",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Host": "api.clickanddrop.royalmail.com",
        "X-Partner-Token": "0000-0000-0000-0000"
    },
    "parameters": {
        "country": {
            "value": "GB",
            "in": "query"
        },
        "weight": {
            "value": "1000",
            "in": "query"
        }
    }
}

ROYAL_MAIL_BAD_REQUEST_RATING_RESPONSE = {
    "status_code": 400,
    "headers": {
        "Transfer-Encoding": "chunked",
        "Content-Type": "application/json; charset=utf-8",
        "Content-Encoding": "gzip",
        "Vary": "Accept-Encoding",
        "AccessToken": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X-Correlation-Id": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Referrer-Policy": "no-referrer",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "SAMEORIGIN",
        "X-XSS-Protection": "1; mode=block",
        "Date": "Wed, 16 Jul 2025 14:04:27 GMT"
    },
    "body": {
        "associatedErrors": [
            "country: The field country must match the regular expression '^([A-Za-z]{3})$'."
        ],
        "errorCode": "INVALID_PARAMETERS",
        "errorDescription": "BAD_REQUEST_MESSAGE_SINGLE_ERROR"
    }
}